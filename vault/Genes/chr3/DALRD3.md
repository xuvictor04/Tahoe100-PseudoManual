---
symbol: "DALRD3"
type: "gene"
col: 10901
ensembl_id: "ENSG00000178149"
name: "DALR anticodon binding domain containing 3"
location: "3p21.31"
module: 93
arm: "+"
pooled_cpm: 10.22
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# DALRD3

*DALR anticodon binding domain containing 3* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +12.0, q 4e-30, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.642× (z -3.9, q 0.029, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPSB2]] (+0.71, fdr 7e-06), [[GTF2B]] (+0.67, fdr 1e-05), [[FAM53C]] (+0.66, fdr 7e-06); moves opposite to [[MRPL42]] (-0.65, fdr 1e-05), [[TMEM33]] (-0.57, fdr 2e-05), [[PRPF19]] (-0.54, fdr 7e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MRC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10901.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +12.0 | 4e-30 | 43/46 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.92×** | +6.2 | 2e-07 | 22/35 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.95×** | +6.1 | 2e-07 | 12/19 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +4.8 | 3e-04 | 21/48 (J82, RPMI-7951, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +4.6 | 4e-04 | 24/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.6 | 4e-04 | 14/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.33×** | +3.8 | 0.010 | 20/45 (NCI-H1573, LoVo, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.48×** | +3.5 | 0.037 | 17/47 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.39× | +3.1 | 0.11 | 14/47 (LoVo, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10901.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.642×** | -3.9 | 0.029 | 23/46 (SW 900, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.666×** | -3.9 | 0.029 | 21/46 (BT-474, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.676×** | -3.7 | 0.029 | 16/44 (H4, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.677×** | -3.7 | 0.029 | 22/44 (RKO, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.668×** | -3.5 | 0.044 | 18/46 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.782×** | -3.3 | 0.078 | 19/48 (H4, CHP-212, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.707×** | -3.3 | 0.078 | 17/47 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.520×** | -3.3 | 0.079 | 15/45 (Panc 03.27, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.728× | -3.0 | 0.15 | 14/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10901. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 7.30 | 0 | 1 | — | [[crizotinib (drug)]] 5 µM 0.0464× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 7.78 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.70× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 7.49 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.43× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 9.62 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.38× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[RKO (line)]] | wt | 8.02 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +11.5) | — |
| [[A-172 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10901), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPSB2]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[GTF2B]] | +0.67 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[FAM53C]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[LRRC23]] | +0.65 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[STX5-DT]] | +0.65 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[TOB2]] | +0.61 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[COQ10B]] | +0.61 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[SELENOW]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[WDR47]] | +0.60 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[TUBB3]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[IKZF4]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[KDM5B]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL42]] | -0.65 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.57 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[PRPF19]] | -0.54 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[TSEN15]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[INTS7]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[RPE]] | -0.53 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[EEF1E1]] | -0.52 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[PPP5C]] | -0.52 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[GOT2]] | -0.52 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[BMS1P2]] | -0.52 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[TCOF1]] | -0.51 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ABHD13]] | -0.51 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRC2]] | B | MRC2 activity raises DALRD3's level | lines that do not express MRC2 (17) vs lines expressing it (33) | 1.34× lower at baseline in the lines without MRC2 | 0.036 | ⚠ within organs, on part of the lines; also absent: FBXO17, ENSG00000269547, FSD1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.7, -25.8); signed map (3.0, 16.4). **Vector** length 64.1, 11.4% of its response variance represented; |z| ≥ 3 in 704 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +12.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.9 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +2.3 | +3.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +1.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +0.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.2 | +0.6 |
|  | [[Demeclocycline (drug)]] 0.05 µM |  | +1.1 | +0.5 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +1.1 | +1.6 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | +1.0 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -3.0 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.5 | +0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | DALR anticodon binding domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,015,488-49,022,293 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10496 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5D0E6](https://www.uniprot.org/uniprotkb/Q5D0E6) (DALR anticodon-binding domain-containing protein 3):

> Involved in tRNA methylation. Facilitates the recognition and targeting of tRNA(Arg)(CCU) and tRNA(Arg)(UCU) substrates for N(3)-methylcytidine modification by METTL2A and METTL2B.

**Summary**, from NCBI Gene [55152](https://www.ncbi.nlm.nih.gov/gene/55152):

> The exact function of this gene is not known. It encodes a protein with a DALR anticodon binding domain similar to that of class Ia aminoacyl tRNA synthetases. This gene is located in a cluster of genes (with a complex sense-anti-sense genome architecture) on chromosome 3, and contains two micro RNA (miRNA) precursors (mir-425 and mir-191) in one of its introns. Preferential expression of this gene (the miRNAs and other genes in the cluster) in testis suggests a role of this gene in …

**Accessions** — [HGNC:25536](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25536) · Entrez [55152](https://www.ncbi.nlm.nih.gov/gene/55152) · UniProt [Q5D0E6](https://www.uniprot.org/uniprotkb/Q5D0E6) · Ensembl [ENSG00000178149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178149)

## Data

Gene col 10901: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10901); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10901, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10901]; `tensor/DDL_lfc|DDL_z.npy` [10901]; `embed/gene_vectors.npy` [10901]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10901 or target_col == 10901). Every well: [[DALRD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DALRD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
