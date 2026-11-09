---
symbol: "UBL7-DT"
type: "gene"
col: 14489
ensembl_id: "ENSG00000247240"
name: "UBL7 divergent transcript"
location: "15q24.1"
module: 71
arm: "+"
pooled_cpm: 9.11
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# UBL7-DT

*UBL7 divergent transcript* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.62× (z +23.7, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.583× (z -7.1, q 1e-09, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C21orf58]] (+0.79, fdr 7e-06), [[XNDC1N]] (+0.67, fdr 7e-06), [[GPR19]] (+0.66, fdr 7e-06); moves opposite to [[RPAP3]] (-0.54, fdr 3e-04), [[KBTBD6]] (-0.49, fdr 3e-04).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14489.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.62×** | +23.7 | 0e+00 | 43/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +12.5 | 2e-33 | 37/41 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +9.6 | 2e-19 | 29/43 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.92×** | +8.5 | 3e-15 | 34/46 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.87×** | +7.5 | 5e-12 | 14/26 (SW480, SW1417, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.77×** | +7.4 | 1e-11 | 28/46 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.0 | 3e-10 | 25/47 (SW1417, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.69×** | +6.9 | 5e-10 | 28/46 (A498, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +4.9 | 7e-05 | 15/46 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.38×** | +4.1 | 0.003 | 9/17 (LOX-IMVI, BT-474, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +3.8 | 0.007 | 11/42 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.22×** | +3.7 | 0.011 | 8/47 (NCI-H2030, A-427, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.31×** | +3.6 | 0.016 | 14/46 (A-427, NCI-H1792, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.31×** | +3.5 | 0.019 | 7/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +3.4 | 0.023 | 4/45 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.038 | 9/45 (KATO III, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.038 | 9/46 (BT-474, HT-29, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.062 | 7/46 (LoVo, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.065 | 4/44 (KATO III, HCT15, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.079 | 3/46 (PANC-1, HT-29, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.17× | +3.0 | 0.079 | 6/47 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.24×** | +2.8 | 0.099 | 4/45 (HCT15, SW48, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14489.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.583×** | -7.1 | 1e-09 | 27/46 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.594×** | -6.8 | 3e-09 | 25/46 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.599×** | -6.7 | 3e-09 | 24/43 (NCI-H1573, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.583×** | -6.6 | 3e-09 | 25/44 (Hs 766T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.601×** | -6.6 | 3e-09 | 23/46 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.646×** | -5.7 | 1e-06 | 21/43 (PANC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.656×** | -5.5 | 3e-06 | 22/46 (C-33 A, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.670×** | -5.2 | 1e-05 | 19/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.542×** | -4.2 | 0.002 | 15/39 (MIA PaCa-2, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.725×** | -4.0 | 0.004 | 13/46 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.745×** | -3.8 | 0.006 | 9/46 (A498, CFPAC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.754×** | -3.7 | 0.011 | 13/46 (RKO, PANC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.759×** | -3.6 | 0.013 | 17/45 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.826×** | -3.5 | 0.017 | 11/47 (SK-MEL-2, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.52 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.5 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +14.1) | [[Digitoxin (drug)]] 5 µM 0.215× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.231× (z -10.9) |
| [[Hs 766T (line)]] | wt | 6.71 | 0 | 3 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0779× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 12.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -9.8) |
| [[SW480 (line)]] | alt | 14.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +15.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.18 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +8.8) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.127× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 8.39 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 6.14 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +12.2) | [[Methotrexate (drug)]] 0.05 µM 0.0498× (z -13.0) |
| [[BT-474 (line)]] | alt | 8.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.52× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 5.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 9.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 7.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +9.0) | — |
| [[KATO III (line)]] | alt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +10.2) | — |
| [[LoVo (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +13.2) | — |
| [[NCI-H1792 (line)]] | alt | 8.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 9.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 3.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 5.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +8.9) | — |
| [[RKO (line)]] | wt | 8.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.37× (z +11.2) | — |
| [[A-172 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C21orf58]] | +0.79 | +0.71 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[XNDC1N]] | +0.67 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[GPR19]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[RMI2]] | +0.64 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[ASF1B]] | +0.64 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[BRCA1]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[PRIMPOL]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SPC25]] | +0.63 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[RAD51AP1]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[ESCO2]] | +0.62 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[DBF4B]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[CENPO]] | +0.61 | +0.42 / +0.66 | both halves | 4e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPAP3]] | -0.54 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[KBTBD6]] | -0.49 | -0.27 / -0.40 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UBL7-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.5, -46.7); signed map (-41.2, -47.5). **Vector** length 68.0, 11.5% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +23.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +12.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +7.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.1 | +1.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +1.1 | +2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.1 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -6.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.3 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | +0.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -4.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | UBL7 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q24.1 — chr15:74,461,248-74,513,971 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously UBL7-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [440288](https://www.ncbi.nlm.nih.gov/gene/440288):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:48614](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48614) · Entrez [440288](https://www.ncbi.nlm.nih.gov/gene/440288) · Ensembl [ENSG00000247240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247240)

## Data

Gene col 14489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14489); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14489]; `tensor/DDL_lfc|DDL_z.npy` [14489]; `embed/gene_vectors.npy` [14489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14489 or target_col == 14489). Every well: [[UBL7-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBL7-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
