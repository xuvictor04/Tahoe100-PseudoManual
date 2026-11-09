---
symbol: "TMEM25"
type: "gene"
col: 7393
ensembl_id: "ENSG00000149582"
name: "transmembrane protein 25"
location: "11q23.3"
module: 47
arm: "+"
pooled_cpm: 5.03
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# TMEM25

*transmembrane protein 25* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.39× (z +12.1, q 6e-31, up in 25 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.359× (z -9.9, q 3e-20, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC36]] (+0.91, fdr 7e-06, ⚠ same locus), [[LINC02236]] (+0.80, fdr 7e-06), [[PITRM1-AS1]] (+0.80, fdr 7e-06), [[MSANTD1]] (+0.78, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7393.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.39×** | +12.1 | 6e-31 | 25/37 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +7.0 | 6e-10 | 20/38 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +6.0 | 3e-07 | 5/21 (KATO III, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +5.5 | 4e-06 | 3/15 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.3 | 1e-05 | 4/10 (NCI-H2347, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +5.3 | 1e-05 | 16/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +5.0 | 4e-05 | 18/45 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.7 | 2e-04 | 8/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.55×** | +4.3 | 0.001 | 7/47 (A498, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7393.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.359×** | -9.9 | 3e-20 | 36/45 (PANC-1, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.438×** | -8.1 | 2e-13 | 30/47 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.439×** | -7.9 | 4e-13 | 29/45 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.450×** | -6.6 | 5e-09 | 23/46 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.610×** | -4.8 | 1e-04 | 22/35 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.615×** | -4.6 | 5e-04 | 13/29 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.664×** | -3.8 | 0.012 | 9/44 (LOX-IMVI, C-33 A, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **0.670×** | -3.8 | 0.012 | 16/43 (A-172, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.672×** | -3.3 | 0.065 | 15/46 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.792×** | -3.2 | 0.074 | 7/47 (LS 180, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -3.2 | 0.074 | 10/44 (LOX-IMVI, HepG2/C3A, …) | top dose only |  |
| [[Bexarotene (drug)]] 5 µM |  | **0.723×** | -3.2 | 0.074 | 7/47 (A-427, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 7.10 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0441× (z -11.8) |
| [[SW480 (line)]] | alt | 6.71 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -10.3) |
| [[A-172 (line)]] | wt | 3.77 | 0 | 2 | — | [[Lopinavir (drug)]] 5 µM 0.0472× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 13.0 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0271× (z -17.3) |
| [[LOX-IMVI (line)]] | wt | 8.15 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0654× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0664× (z -10.1) |
| [[PANC-1 (line)]] | alt | 3.95 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.135× (z -8.9) |
| [[A-427 (line)]] | wt | 4.58 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0969× (z -9.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 4.33 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0329× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 7.70 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0533× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -10.5) |
| [[A498 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC36]] | +0.91 | +0.86 / +0.88 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC02236]] | +0.80 | +0.81 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PITRM1-AS1]] | +0.80 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[MSANTD1]] | +0.78 | +0.76 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PILRA]] | +0.78 | +0.78 / +0.78 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.78 | +0.84 / +0.71 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.78 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[SGSM3-AS1]] | +0.78 | +0.74 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[KIF17]] | +0.78 | +0.78 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[PYGM]] | +0.77 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.77 | +0.81 / +0.77 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[USP50]] | +0.76 | +0.78 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2]] | B | F2 activity raises TMEM25's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.76× lower at baseline in the lines without F2 | 0.012 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LMO7DN]] | B | LMO7DN activity raises TMEM25's level | lines that do not express LMO7DN (14) vs lines expressing it (36) | 1.32× lower at baseline in the lines without LMO7DN | 0.085 | ⚠ within organs, on part of the lines; also absent: LMO7, IL1RN, KITLG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.831). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.6, -15.1); signed map (17.6, 12.0). **Vector** length 70.4, 11.2% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +7.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | -9.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.6 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.2 | -8.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -4.8 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.1 | -6.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.6 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,531,041-118,547,280 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14399 |
| Gene groups (HGNC) | C2-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YD3](https://www.uniprot.org/uniprotkb/Q86YD3) (Transmembrane protein 25):

> In neurons, modulates the degradation of NMDA receptor GRIN2B subunit. Plays a role in the regulation of neuronal excitability.

**Summary**, from NCBI Gene [84866](https://www.ncbi.nlm.nih.gov/gene/84866):

> Predicted to be involved in negative regulation of excitatory postsynaptic potential and regulation of protein stability. Predicted to be located in late endosome and lysosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25890](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25890) · Entrez [84866](https://www.ncbi.nlm.nih.gov/gene/84866) · UniProt [Q86YD3](https://www.uniprot.org/uniprotkb/Q86YD3) · Ensembl [ENSG00000149582](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149582)

## Data

Gene col 7393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7393); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7393]; `tensor/DDL_lfc|DDL_z.npy` [7393]; `embed/gene_vectors.npy` [7393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7393 or target_col == 7393). Every well: [[TMEM25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
