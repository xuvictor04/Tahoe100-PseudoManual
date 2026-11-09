---
symbol: "DYRK4"
type: "gene"
col: 200
ensembl_id: "ENSG00000010219"
name: "dual specificity tyrosine phosphorylation regulated kinase 4"
location: "12p13.32"
module: 71
arm: "+"
pooled_cpm: 12.21
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# DYRK4

*dual specificity tyrosine phosphorylation regulated kinase 4* — 12p13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.61× (z +25.2, q 0e+00, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.525× (z -6.3, q 2e-07, down in 18 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMI1]] (+0.71, fdr 7e-06), [[RAD51AP1]] (+0.70, fdr 7e-06, ⚠ same locus), [[DNAJC9]] (+0.69, fdr 7e-06), [[RMI2]] (+0.68, fdr 9e-06); moves opposite to [[SMIM30]] (-0.55, fdr 2e-04), [[TBC1D19]] (-0.51, fdr 2e-04), [[STX8]] (-0.50, fdr 4e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 200.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +25.2 | 0e+00 | 41/44 (SW 900, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.66×** | +23.2 | 0e+00 | 38/44 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +20.2 | 0e+00 | 35/44 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +10.9 | 2e-25 | 27/39 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.58×** | +7.9 | 3e-13 | 15/29 (NCI-H460, KATO III, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.5 | 8e-09 | 19/45 (PANC-1, SW1417, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.30×** | +4.9 | 7e-05 | 13/34 (Panc 03.27, NCI-H23, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 5e-04 | 14/43 (A-427, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.23×** | +3.8 | 0.011 | 7/22 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.012 | 5/46 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.032 | 11/42 (NCI-H23, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +3.3 | 0.042 | 15/45 (LoVo, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 1.19× | +3.3 | 0.044 | 10/45 (MIA PaCa-2, J82, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.13× | +3.2 | 0.065 | 8/45 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.18× | +3.0 | 0.090 | 9/45 (A498, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 200.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.525×** | -6.3 | 2e-07 | 18/46 (SW480, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.546×** | -5.9 | 1e-06 | 17/43 (A-427, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.761×** | -4.8 | 3e-04 | 14/44 (HCT15, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.780×** | -4.6 | 5e-04 | 11/45 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.707×** | -4.6 | 5e-04 | 5/45 (SNU-1, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.800×** | -4.1 | 0.003 | 11/45 (A-172, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.824×** | -3.4 | 0.052 | 5/45 (NCI-H460, COLO 205, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.886× | -3.2 | 0.10 | 10/46 (SW48, H4, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | 0.726× | -3.1 | 0.11 | 4/42 (H4, HCT15, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.845× | -3.0 | 0.15 | 5/44 (LS 180, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 10.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +13.4) | — |
| [[SW480 (line)]] | alt | 17.1 | 3 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.46× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 12.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.13× (z +13.3) | — |
| [[RKO (line)]] | wt | 13.1 | 3 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 11.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.51× (z +14.3) | — |
| [[BT-474 (line)]] | alt | 8.55 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0680× (z -10.3) |
| [[C32 (line)]] | wt | 13.6 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 7.24× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 20.4 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.30× (z +14.2) | — |
| [[J82 (line)]] | alt | 12.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.45× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 14.5 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 18.2 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +15.6) | — |
| [[NCI-H23 (line)]] | alt | 29.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 11.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +11.3) | — |
| [[A-427 (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -8.7) ⚠ cell-cycle shift, explains ~11% of this change |
| [[H4 (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.147× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 20.0 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.161× (z -8.7) |
| [[HT-29 (line)]] | alt | 6.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +12.7) | — |
| [[NCI-H460 (line)]] | wt | 10.5 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 9.68 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0917× (z -10.3) |
| [[SNU-423 (line)]] | alt | 5.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +9.6) | — |
| [[SW48 (line)]] | wt | 19.2 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0782× (z -11.3) |
| [[A-172 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMI1]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[RAD51AP1]] | +0.70 | +0.61 / +0.77 | both halves | 7e-06 | ⚠ same locus (2.2 kb, same strand: neighbours can correlate without regulation) |
| [[DNAJC9]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[RMI2]] | +0.68 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[PRIMPOL]] | +0.68 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[DONSON]] | +0.66 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[FANCM]] | +0.65 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[GSTCD]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[C21orf58]] | +0.64 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[ZNF367]] | +0.64 | +0.47 / +0.73 | both halves | 2e-05 |  |
| [[CDCA5]] | +0.64 | +0.53 / +0.74 | both halves | 1e-05 |  |
| [[DDIAS]] | +0.63 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[KNTC1]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM30]] | -0.55 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[TBC1D19]] | -0.51 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[STX8]] | -0.50 | -0.40 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DYRK4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TP53]] | C | TP53 activity weakens DYRK4's drug response | recorded loss-of-function mutation of TP53 in 29 lines vs 17 not recorded | the TP53-altered lines respond 1.52× as strongly (z diff -1.17); strongest at Mitoxantrone (dihydrochloride) 5 µM: 1.55x vs 0.96x (z diff -3.4) | 0.834 over the table, 0.064 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.7, -46.2); signed map (-41.2, -48.0). **Vector** length 82.1, 15.1% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.59 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +23.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +20.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +25.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +2.0 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -3.9 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -5.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity tyrosine phosphorylation regulated kinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.32 — chr12:4,562,208-4,615,302 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Dual-specificity tyrosine-regulated kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR20](https://www.uniprot.org/uniprotkb/Q9NR20) (Dual specificity tyrosine-phosphorylation-regulated kinase 4):

> Possible non-essential role in spermiogenesis.

**Summary**, from NCBI Gene [8798](https://www.ncbi.nlm.nih.gov/gene/8798):

> This gene encodes an enzyme that belongs to a conserved family of serine/threonine protein kinases. Members of this dual specificity kinase family are thought to function in the regulation of cell differentiation and proliferation, survival, and in development. Alternate splicing results in multiple transcript variants. Additional alternatively spliced transcript variants of this gene have been described, but their full-length nature is not known. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:3095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3095) · Entrez [8798](https://www.ncbi.nlm.nih.gov/gene/8798) · UniProt [Q9NR20](https://www.uniprot.org/uniprotkb/Q9NR20) · Ensembl [ENSG00000010219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010219)

## Data

Gene col 200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 200); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 200]; `tensor/DDL_lfc|DDL_z.npy` [200]; `embed/gene_vectors.npy` [200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 200 or target_col == 200). Every well: [[DYRK4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYRK4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
