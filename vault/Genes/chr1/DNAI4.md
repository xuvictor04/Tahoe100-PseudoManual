---
symbol: "DNAI4"
type: "gene"
col: 7654
ensembl_id: "ENSG00000152763"
name: "dynein axonemal intermediate chain 4"
location: "1p31.3"
module: 23
arm: "+"
pooled_cpm: 12.48
n_lines_expressing: 49
n_dd_up: 42
n_dd_down: 2
n_dd_up_clean: 39
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# DNAI4

*dynein axonemal intermediate chain 4* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.41× (z +25.8, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.594× (z -5.1, q 2e-04, down in 24 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.173×; ⚠ toxic; transcription drop); [[Posaconazole (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0518×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (NCI-H2347 0.0789×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD17-DT]] (+0.85, fdr 7e-06), [[CASS4]] (+0.83, fdr 7e-06), [[CHD1-DT]] (+0.83, fdr 7e-06); moves opposite to [[WASF3]] (-0.71, fdr 1e-04), [[NAPG]] (-0.70, fdr 3e-05), [[PRR5]] (-0.67, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KIF21B]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PATL2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7654.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.41×** | +25.8 | 0e+00 | 43/43 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.18×** | +19.8 | 0e+00 | 40/42 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **6.01×** | +16.9 | 0e+00 | 40/42 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.09×** | +13.3 | 4e-38 | 39/42 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.51×** | +12.3 | 8e-33 | 41/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.00×** | +10.4 | 3e-23 | 33/36 (NCI-H1573, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.84×** | +8.4 | 3e-15 | 34/47 (HOP62, SW1417, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.36×** | +8.1 | 4e-14 | 37/46 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.15×** | +7.5 | 4e-12 | 35/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +6.9 | 2e-10 | 26/47 (A498, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +5.6 | 1e-06 | 23/46 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +5.3 | 7e-06 | 20/45 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +4.8 | 8e-05 | 24/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.62×** | +4.7 | 1e-04 | 16/47 (SNU-423, A-172, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 1e-04 | 20/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.57×** | +4.5 | 3e-04 | 15/47 (LoVo, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7654.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.173×; ⚠ toxic; transcription drop); [[Posaconazole (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0518×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (NCI-H2347 0.0789×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.594×** | -5.1 | 2e-04 | 24/46 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.641×** | -4.4 | 0.003 | 21/46 (SW1417, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.532× | -3.2 | 0.17 | 12/45 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.721× | -3.2 | 0.17 | 12/47 (SW 1271, SW 1088, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.725× | -3.0 | 0.23 | 17/44 (H4, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7654. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 17.2 | 5 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 18.3× (z +14.5) | — |
| [[SW480 (line)]] | alt | 11.1 | 5 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +14.9) | — |
| [[NCI-H2347 (line)]] | alt | 3.79 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.63× (z +9.9) | [[Glycyrrhizic acid (drug)]] 5 µM 0.0789× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 41.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -11.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 8.61 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.72× (z +11.6) | — |
| [[LoVo (line)]] | wt | 6.39 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +15.6) | — |
| [[LOX-IMVI (line)]] | wt | 12.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.84× (z +14.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.24× (z +13.1) | — |
| [[Panc 03.27 (line)]] | alt | 7.27 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.92× (z +12.2) | — |
| [[PANC-1 (line)]] | alt | 16.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.40× (z +15.6) | — |
| [[RPMI-7951 (line)]] | alt | 15.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +9.2) | — |
| [[A498 (line)]] | wt | 11.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.14× (z +11.1) | — |
| [[C32 (line)]] | wt | 12.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 7.75 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.60× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 22.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 10.00 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.16× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 24.5 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 9.71 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.28× (z +8.9) | [[Posaconazole (drug)]] 0.5 µM 0.0518× (z -10.1) |
| [[KATO III (line)]] | alt | 8.94 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 7.49× (z +9.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.68× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 7.40 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 28.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +12.6) | — |
| [[RKO (line)]] | wt | 8.25 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +12.1) | — |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 7.45 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.28× (z +12.2) | — |
| [[SW 900 (line)]] | alt | 7.40 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.06× (z +11.2) | — |
| [[A-172 (line)]] | wt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +9.9) | — |
| [[A549 (line)]] | wt | 4.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.55× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 4.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.3× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 26.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +10.7) | — |
| [[H4 (line)]] | wt | 7.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.15× (z +13.1) | — |
| [[HepG2_C3A (line)]] | wt | 8.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.74× (z +10.1) | — |
| [[J82 (line)]] | alt | 9.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.65× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 6.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.99× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 7.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 6.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.2× (z +14.9) | — |
| [[A-427 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7654), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD17-DT]] | +0.85 | +0.85 / +0.64 | both halves | 7e-06 |  |
| [[CASS4]] | +0.83 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[CHD1-DT]] | +0.83 | +0.84 / +0.62 | both halves | 7e-06 |  |
| [[CCDC30]] | +0.80 | +0.82 / +0.55 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.80 | +0.80 / +0.51 | both halves | 1e-05 |  |
| [[GALNT7-DT]] | +0.79 | +0.80 / +0.44 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.79 | +0.82 / +0.37 | both halves | 8e-05 |  |
| [[RFX3-DT]] | +0.79 | +0.82 / +0.47 | both halves | 2e-05 |  |
| [[ENTPD3-AS1]] | +0.78 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[NIFK-AS1]] | +0.78 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[HEXIM2-AS1]] | +0.78 | +0.77 / +0.38 | both halves | 6e-05 |  |
| [[AHI1-DT]] | +0.77 | +0.76 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASF3]] | -0.71 | -0.69 / -0.33 | both halves | 1e-04 |  |
| [[NAPG]] | -0.70 | -0.72 / -0.45 | both halves | 3e-05 |  |
| [[PRR5]] | -0.67 | -0.69 / -0.45 | both halves | 3e-05 |  |
| [[GPRIN1]] | -0.65 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[CAMK2G]] | -0.65 | -0.60 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF21B]] | B | KIF21B activity lowers DNAI4's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 1.44× higher at baseline in the lines without KIF21B | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DNAI4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PATL2]] | C | DNAI4's natural level strengthens PATL2's drug response | DNAI4's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.16; direction not clear | 0.055 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.854). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.5, 16.7); signed map (26.6, -8.4). **Vector** length 109, 28.8% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +12.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +16.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +25.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +19.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +13.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +7.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.1 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +3.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.2 | +1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.6 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.5 | +1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -2.0 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal intermediate chain 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:66,812,885-66,924,856 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DIC4, FLJ23129; previously WDR78 |
| Gene groups (HGNC) | WD repeat domain containing; Dyneins, axonemal inner arm I1/f complex subunits; Dynein intermediate chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VTH9](https://www.uniprot.org/uniprotkb/Q5VTH9) (Dynein axonemal intermediate chain 4):

> Plays a critical role in the assembly of axonemal dynein complex, thereby playing a role in ciliary motility.

**Summary**, from NCBI Gene [79819](https://www.ncbi.nlm.nih.gov/gene/79819):

> Predicted to enable dynein heavy chain binding activity and dynein light chain binding activity. Predicted to be involved in axonemal dynein complex assembly and cilium movement. Predicted to act upstream of or within hematopoietic progenitor cell differentiation. Predicted to be located in axoneme; dynein axonemal particle; and motile cilium. Predicted to be part of axonemal dynein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26252](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26252) · Entrez [79819](https://www.ncbi.nlm.nih.gov/gene/79819) · UniProt [Q5VTH9](https://www.uniprot.org/uniprotkb/Q5VTH9) · Ensembl [ENSG00000152763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152763)

## Data

Gene col 7654: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7654); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7654, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7654]; `tensor/DDL_lfc|DDL_z.npy` [7654]; `embed/gene_vectors.npy` [7654]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7654 or target_col == 7654). Every well: [[DNAI4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAI4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
