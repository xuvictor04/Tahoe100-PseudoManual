---
symbol: "FAM89B"
type: "gene"
col: 10773
ensembl_id: "ENSG00000176973"
name: "family with sequence similarity 89 member B"
location: "11q13.1"
module: 192
arm: "+"
pooled_cpm: 6.71
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# FAM89B

*family with sequence similarity 89 member B* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 2.10× (z +4.8, q 9e-04, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.385× (z -6.1, q 5e-07, down in 33 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.538× (z -5.6, q 5e-06, down in 24 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKN2D]] (+0.75, fdr 7e-06), [[CIB1]] (+0.74, fdr 7e-06), [[POLD4]] (+0.73, fdr 7e-06); moves opposite to [[FUBP1]] (-0.71, fdr 1e-05), [[SNX5]] (-0.69, fdr 1e-05), [[EWSR1]] (-0.66, fdr 1e-05).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10773.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **2.10×** | +4.8 | 9e-04 | 29/37 (HEC-1-A, LS 180, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +4.6 | 0.001 | 24/44 (Panc 03.27, KATO III, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.05×** | +4.4 | 0.002 | 6/16 (A498, J82, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.95×** | +4.2 | 0.003 | 11/28 (NCI-H1792, SNU-423, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +4.0 | 0.008 | 22/44 (Panc 03.27, SW480, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.83×** | +3.9 | 0.009 | 17/35 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +3.8 | 0.010 | 21/44 (Panc 03.27, KATO III, …) | all doses, flat | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10773.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.385×** | -6.1 | 5e-07 | 33/44 (PANC-1, NCI-H2347, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.538×** | -5.6 | 5e-06 | 24/39 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.428×** | -5.4 | 1e-05 | 33/45 (NCI-H1792, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.512×** | -4.3 | 0.002 | 23/35 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.526×** | -4.1 | 0.004 | 22/44 (Hs 766T, SW1417, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.535×** | -4.0 | 0.006 | 20/43 (C32, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.279×** | -4.0 | 0.006 | 24/40 (A-427, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.587×** | -3.4 | 0.046 | 19/42 (NCI-H1792, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.572×** | -3.4 | 0.046 | 20/43 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.602×** | -3.2 | 0.074 | 17/43 (A-172, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.593×** | -3.2 | 0.079 | 17/41 (SK-MEL-2, A-172, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.707×** | -3.1 | 0.079 | 23/43 (HT-29, RPMI-7951, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10773. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 5.89 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0352× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 12.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -11.4) |
| [[C32 (line)]] | wt | 8.55 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0268× (z -12.5) |
| [[HOP62 (line)]] | alt | 8.02 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -8.8) |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 6.49 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0776× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10773), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2D]] | +0.75 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[CIB1]] | +0.74 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[POLD4]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[CARD19]] | +0.72 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[RRAS]] | +0.72 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[PLIN3]] | +0.72 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[TRPT1]] | +0.71 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[CARHSP1]] | +0.68 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[GNAI2]] | +0.67 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.66 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.66 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[FRMD8]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 | STRING 546 |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP1]] | -0.71 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[SNX5]] | -0.69 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[EWSR1]] | -0.66 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[RCN1]] | -0.65 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[SUCLG2]] | -0.65 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[NNT]] | -0.64 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[MCCC2]] | -0.64 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[HDDC2]] | -0.63 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[MTHFSD]] | -0.62 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[SRSF1]] | -0.62 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[RAB11FIP2]] | -0.62 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[UTP20]] | -0.61 | -0.46 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers FAM89B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.850). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.1, 1.8); signed map (-28.4, 16.4). **Vector** length 83.8, 20.3% of its response variance represented; |z| ≥ 3 in 795 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.5 | +4.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.4 | +4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +3.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.3 | +2.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.4 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -4.3 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -3.9 | +4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.8 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.3 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 89 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,572,349-65,574,198 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTVR1, LRAP25 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5H3](https://www.uniprot.org/uniprotkb/Q8N5H3) (Leucine repeat adapter protein 25):

> Negatively regulates TGF-beta-induced signaling; in cooperation with SKI prevents the translocation of SMAD2 from the nucleus to the cytoplasm in response to TGF-beta. Acts as an adapter that mediates the specific recognition of LIMK1 by CDC42BPA and CDC42BPB in the lamellipodia. LRAP25-mediated CDC42BPA/CDC42BPB targeting to LIMK1 and the lamellipodium results in LIMK1 activation and the subsequent phosphorylation of CFL1 which is important for lamellipodial F-actin regulation.

**Summary**, from NCBI Gene [23625](https://www.ncbi.nlm.nih.gov/gene/23625):

> Predicted to enable transcription corepressor binding activity. Predicted to be involved in establishment of cell polarity; negative regulation of transmembrane receptor protein serine/threonine kinase signaling pathway; and positive regulation of cell migration. Predicted to be active in cytoplasm and lamellipodium. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16708) · Entrez [23625](https://www.ncbi.nlm.nih.gov/gene/23625) · UniProt [Q8N5H3](https://www.uniprot.org/uniprotkb/Q8N5H3) · Ensembl [ENSG00000176973](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176973)

## Data

Gene col 10773: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10773); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10773, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10773]; `tensor/DDL_lfc|DDL_z.npy` [10773]; `embed/gene_vectors.npy` [10773]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10773 or target_col == 10773). Every well: [[FAM89B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM89B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
