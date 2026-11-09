---
symbol: "PAIP2B"
type: "gene"
col: 4524
ensembl_id: "ENSG00000124374"
name: "poly(A) binding protein interacting protein 2B"
location: "2p13.3"
module: 1
arm: "-"
pooled_cpm: 5.97
n_lines_expressing: 43
n_dd_up: 29
n_dd_down: 11
n_dd_up_clean: 22
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PAIP2B

*poly(A) binding protein interacting protein 2B* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 7.58× (z +27.1, q 0e+00, up in 40 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.521× (z -8.7, q 1e-15, down in 18 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.621× (z -6.4, q 3e-08, down in 15 of 37 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLAG1]] (+0.64, fdr 3e-05), [[MXI1]] (+0.63, fdr 1e-04), [[MINDY2]] (+0.63, fdr 4e-05); moves opposite to [[E2F6]] (-0.61, fdr 3e-05), [[COMMD10]] (-0.60, fdr 7e-05), [[BICD1]] (-0.59, fdr 4e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4524.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **7.58×** | +27.1 | 0e+00 | 40/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.91×** | +25.9 | 0e+00 | 38/38 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.74×** | +25.0 | 0e+00 | 35/35 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.19×** | +24.4 | 0e+00 | 39/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.36×** | +16.2 | 0e+00 | 37/40 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.77×** | +13.1 | 3e-37 | 24/30 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +10.8 | 2e-25 | 27/33 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.19×** | +10.5 | 6e-24 | 29/35 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.96×** | +9.6 | 4e-20 | 32/36 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +8.2 | 2e-14 | 7/11 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +7.6 | 1e-12 | 16/34 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +7.5 | 4e-12 | 22/39 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.1 | 4e-11 | 15/40 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.57×** | +6.1 | 6e-08 | 19/39 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +5.9 | 1e-07 | 14/39 (LS 180, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 3e-06 | 9/38 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4524.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.521×** | -8.7 | 1e-15 | 18/34 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.611×** | -6.6 | 1e-08 | 17/39 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.621×** | -6.4 | 3e-08 | 15/37 (LS 180, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.623×** | -6.3 | 3e-08 | 20/39 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.661×** | -5.6 | 3e-06 | 13/38 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.522×** | -4.6 | 5e-04 | 12/36 (Panc 03.27, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.557×** | -4.1 | 0.003 | 15/34 (A-172, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.745×** | -4.0 | 0.005 | 9/40 (NCI-H23, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.752×** | -3.6 | 0.019 | 7/37 (Panc 03.27, HEC-1-A, …) | inconsistent across doses |  |
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | **0.831×** | -3.5 | 0.024 | 5/38 (A-427, HOP62, …) | top dose only | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.833×** | -3.5 | 0.026 | 7/40 (NCI-H23, H4, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.799× | -3.0 | 0.12 | 9/38 (SW480, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4524. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.40 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 24.9× (z +14.5) | — |
| [[SW480 (line)]] | alt | 14.4 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.74× (z +13.8) | — |
| [[A498 (line)]] | wt | 1.99 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 27.5× (z +10.7) | [[Bendamustine (drug)]] 0.5 µM 0.0583× (z -9.3) |
| [[HT-29 (line)]] | alt | 8.20 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.35× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 10.1 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.44× (z +11.4) | — |
| [[A-427 (line)]] | wt | 11.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.50× (z +11.1) | — |
| [[A549 (line)]] | wt | 3.30 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 18.6× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 11.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.63× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 9.23 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 11.2× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 3.10 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 15.2× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 7.11 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.87× (z +9.1) | — |
| [[LoVo (line)]] | wt | 6.41 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 4.66 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 7.85 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +9.1) | — |
| [[A-172 (line)]] | wt | 4.31 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 13.1× (z +9.8) | — |
| [[J82 (line)]] | alt | 4.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.45× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 7.36 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.65× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-423 (line)]] | alt | 6.87 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0330× (z -14.9) |
| [[SW 900 (line)]] | alt | 7.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.749 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4524), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAG1]] | +0.64 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[MXI1]] | +0.63 | +0.34 / +0.56 | both halves | 1e-04 |  |
| [[MINDY2]] | +0.63 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[KDM3A]] | +0.63 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[SAP30-DT]] | +0.61 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[ANG]] | +0.60 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[GMCL1]] | +0.60 | +0.26 / +0.61 | both halves | 4e-04 |  |
| [[FOXO4]] | +0.59 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[APAF1]] | +0.59 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[LNX2]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PJA2]] | +0.59 | +0.29 / +0.49 | both halves | 2e-04 |  |
| [[CNOT6L]] | +0.58 | +0.40 / +0.54 | both halves | 5e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F6]] | -0.61 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[COMMD10]] | -0.60 | -0.37 / -0.55 | both halves | 7e-05 |  |
| [[BICD1]] | -0.59 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[RRP7A]] | -0.58 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[PSMD1]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[CHMP6]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[NAA25]] | -0.57 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[NAA15]] | -0.57 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[NIP7]] | -0.56 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[ZNF195]] | -0.56 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[LTV1]] | -0.56 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TANGO6]] | -0.55 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PAIP2B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.517). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.3, -31.1); signed map (-23.8, 15.6). **Vector** length 51.7, 7.28% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +25.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +4.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.7 | +4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +7.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +9.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +1.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | poly(A) binding protein interacting protein 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:71,182,738-71,227,103 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1155 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULR5](https://www.uniprot.org/uniprotkb/Q9ULR5) (Polyadenylate-binding protein-interacting protein 2B):

> Inhibits translation of capped and polyadenylated mRNAs by displacing PABPC1 from the poly(A) tail.

**Summary**, from NCBI Gene [400961](https://www.ncbi.nlm.nih.gov/gene/400961):

> Most mRNAs, except for histones, contain a 3-prime poly(A) tail. Poly(A)-binding protein (PABP; see MIM 604679) enhances translation by circularizing mRNA through its interaction with the translation initiation factor EIF4G1 (MIM 600495) and the poly(A) tail. Various PABP-binding proteins regulate PABP activity, including PAIP1 (MIM 605184), a translational stimulator, and PAIP2A (MIM 605604) and PAIP2B, translational inhibitors (Derry et al., 2006 [PubMed 17381337]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29200) · Entrez [400961](https://www.ncbi.nlm.nih.gov/gene/400961) · UniProt [Q9ULR5](https://www.uniprot.org/uniprotkb/Q9ULR5) · Ensembl [ENSG00000124374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124374)

## Data

Gene col 4524: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4524); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4524, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4524]; `tensor/DDL_lfc|DDL_z.npy` [4524]; `embed/gene_vectors.npy` [4524]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4524 or target_col == 4524). Every well: [[PAIP2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAIP2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
