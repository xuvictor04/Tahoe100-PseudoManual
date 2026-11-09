---
symbol: "RSAD1"
type: "gene"
col: 5863
ensembl_id: "ENSG00000136444"
name: "radical S-adenosyl methionine domain containing 1"
location: "17q21.33"
module: 26
arm: "-"
pooled_cpm: 14.49
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# RSAD1

*radical S-adenosyl methionine domain containing 1* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.50× (z +8.6, q 4e-15, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.485× (z -15.4, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRAT1]] (+0.75, fdr 7e-06), [[ASB13]] (+0.73, fdr 7e-06), [[ACTR5]] (+0.73, fdr 1e-05); moves opposite to [[MMADHC-DT]] (-0.74, fdr 1e-05), [[UBE3B]] (-0.71, fdr 1e-05), [[CCDC90B-AS1]] (-0.71, fdr 4e-05).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +8.6 | 4e-15 | 34/48 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +8.2 | 1e-13 | 33/44 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +7.9 | 7e-13 | 30/47 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +6.3 | 4e-08 | 31/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +5.3 | 1e-05 | 25/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +5.3 | 1e-05 | 24/47 (NCI-H2347, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.58×** | +4.9 | 8e-05 | 24/44 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.7 | 2e-04 | 21/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 7e-04 | 19/44 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.002 | 11/45 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.8 | 0.007 | 9/42 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.7 | 0.010 | 16/42 (hTERT-HPNE, RKO, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.010 | 9/45 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.28×** | +3.7 | 0.010 | 14/40 (A-427, SW480, …) | two highest doses | composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.3 | 0.035 | 8/30 (LoVo, A498, …) | top dose only | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.045 | 7/45 (HEC-1-A, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.072 | 9/45 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Erythromycin (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.096 | 5/47 (A-172, SW1417, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, none with an alert; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5863.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.485×** | -15.4 | 0e+00 | 39/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.496×** | -14.9 | 0e+00 | 37/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.328×** | -8.1 | 2e-13 | 33/48 (PANC-1, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -6.5 | 1e-08 | 25/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.652×** | -6.4 | 1e-08 | 27/48 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.652×** | -6.4 | 1e-08 | 26/46 (HS-578T, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.661×** | -6.2 | 4e-08 | 29/47 (SW 900, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.673×** | -6.0 | 2e-07 | 25/46 (SW 900, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.456×** | -5.7 | 8e-07 | 30/44 (LOX-IMVI, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.768×** | -5.6 | 1e-06 | 24/48 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -5.5 | 2e-06 | 25/46 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.688×** | -5.4 | 3e-06 | 22/46 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.703×** | -5.3 | 5e-06 | 20/47 (LoVo, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.796×** | -3.3 | 0.042 | 13/47 (A-427, SW1417, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.042 | 15/45 (SK-MEL-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -16.5) |
| [[PANC-1 (line)]] | alt | 17.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -19.9) |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0950× (z -21.3) |
| [[A549 (line)]] | wt | 16.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 21.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 12.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 19.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -15.1) |
| [[RKO (line)]] | wt | 29.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -18.7) |
| [[SW48 (line)]] | wt | 26.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.4) |
| [[A498 (line)]] | wt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.3) |
| [[BT-474 (line)]] | alt | 36.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -9.1) |
| [[C32 (line)]] | wt | 10.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -9.3) |
| [[CHP-212 (line)]] | wt | 33.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -8.7) |
| [[HCT15 (line)]] | alt | 7.62 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0467× (z -10.1) |
| [[HS-578T (line)]] | alt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -9.9) |
| [[LoVo (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.3) |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 9.94 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.2) |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0903× (z -12.5) |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -14.0) |
| [[SW480 (line)]] | alt | 13.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -12.2) |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | +0.75 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ASB13]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ACTR5]] | +0.73 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[ZNF692]] | +0.73 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TRABD]] | +0.72 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[BRF1]] | +0.70 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[GTPBP3]] | +0.69 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[METAP1]] | +0.69 | +0.68 / +0.46 | both halves | 3e-05 | STRING 655 |
| [[FXN]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[NLE1]] | +0.68 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[POLRMT]] | +0.68 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[ARRB2]] | +0.68 | +0.46 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC-DT]] | -0.74 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[UBE3B]] | -0.71 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | -0.71 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[PKN2-AS1]] | -0.70 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[PBLD]] | -0.70 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[LINC00571]] | -0.70 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[ATXN1L]] | -0.68 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[MZF1-AS1]] | -0.68 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[FAM120AOS]] | -0.67 | -0.61 / -0.39 | both halves | 5e-05 |  |
| [[CPEB2-DT]] | -0.66 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[PCNX4-DT]] | -0.66 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[ZNF341-AS1]] | -0.66 | -0.56 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RSAD1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.712). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-0.9, -2.3); signed map (-39.0, -17.2). **Vector** length 93.4, 19.7% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +5.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +7.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.9 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.4 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.3 | -15.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -14.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.7 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | radical S-adenosyl methionine domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,478,860-50,485,974 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11164, HemW |
| Gene groups (HGNC) | Radical S-adenosylmethionine domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HA92](https://www.uniprot.org/uniprotkb/Q9HA92) (Radical S-adenosyl methionine domain-containing protein 1, mitochondrial):

> May be a heme chaperone, appears to bind heme. Homologous bacterial proteins do not have oxygen-independent coproporphyrinogen-III oxidase activity (Probable). Binds 1 [4Fe-4S] cluster. The cluster is coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine (By similarity).

**Summary**, from NCBI Gene [55316](https://www.ncbi.nlm.nih.gov/gene/55316):

> Enables heme binding activity. Predicted to be involved in porphyrin-containing compound biosynthetic process. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25634](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25634) · Entrez [55316](https://www.ncbi.nlm.nih.gov/gene/55316) · UniProt [Q9HA92](https://www.uniprot.org/uniprotkb/Q9HA92) · Ensembl [ENSG00000136444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136444)

## Data

Gene col 5863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5863); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5863]; `tensor/DDL_lfc|DDL_z.npy` [5863]; `embed/gene_vectors.npy` [5863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5863 or target_col == 5863). Every well: [[RSAD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSAD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
