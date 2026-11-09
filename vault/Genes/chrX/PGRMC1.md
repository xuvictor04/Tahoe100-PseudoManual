---
symbol: "PGRMC1"
type: "gene"
col: 2181
ensembl_id: "ENSG00000101856"
name: "progesterone receptor membrane component 1"
location: "Xq24"
module: 29
arm: "+"
pooled_cpm: 43.91
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PGRMC1

*progesterone receptor membrane component 1* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.18× (z +22.7, q 0e+00, up in 47 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.11× (z +16.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.810× (z -4.8, q 0.001, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 0.437×, SNU-1 0.245×, H4 0.393×, C-33 A 0.342×); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (C32 0.0776×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.285×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOB1A]] (+0.77, fdr 7e-06), [[SUMO3]] (+0.74, fdr 7e-06), [[AP2M1]] (+0.71, fdr 7e-06); moves opposite to [[ZNF316]] (-0.72, fdr 7e-06), [[MTRES1]] (-0.70, fdr 1e-05), [[PPP1R35]] (-0.67, fdr 7e-06, ⚠ PPP1R35 in the vector space only through flagged drug-doses), [[PRPF38B]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.18×** | +22.7 | 0e+00 | 47/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.02×** | +21.2 | 0e+00 | 36/36 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +16.8 | 0e+00 | 46/48 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.08×** | +16.5 | 0e+00 | 42/43 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +9.3 | 2e-18 | 42/48 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +8.1 | 5e-14 | 8/48 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +7.8 | 6e-13 | 37/47 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +7.5 | 4e-12 | 34/46 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.8 | 5e-10 | 32/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +5.7 | 7e-07 | 32/48 (HOP62, H4, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +5.1 | 2e-05 | 20/48 (CFPAC-1, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +4.9 | 6e-05 | 26/48 (HOP62, H4, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.33×** | +4.5 | 4e-04 | 25/47 (MIA PaCa-2, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +4.4 | 5e-04 | 23/48 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.28×** | +3.8 | 0.006 | 21/47 (NCI-H1573, A-427, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.025 | 18/48 (BT-474, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2181.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 0.437×, SNU-1 0.245×, H4 0.393×, C-33 A 0.342×); [[LY-2584702 (tosylate salt) (drug)]] 5 µM in 1 line (C32 0.0776×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.285×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.810×** | -4.8 | 0.001 | 22/48 (J82, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.785×** | -3.7 | 0.056 | 19/48 (J82, C32, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.756× | -3.2 | 0.21 | 17/47 (HCT15, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.757× | -3.2 | 0.21 | 17/48 (Hs 766T, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.812× | -3.0 | 0.30 | 12/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 53.8 | 9 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +14.2) | — |
| [[SW480 (line)]] | alt | 42.3 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +19.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +12.8) | — |
| [[A-172 (line)]] | wt | 19.0 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 36.7 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +15.3) | — |
| [[HEC-1-A (line)]] | alt | 48.6 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 34.9 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.6) | — |
| [[J82 (line)]] | alt | 72.0 | 4 (3 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 31.8 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.57× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 35.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +11.9) | — |
| [[A498 (line)]] | wt | 93.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +12.9) | — |
| [[A549 (line)]] | wt | 42.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.18× (z +15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +14.2) | — |
| [[H4 (line)]] | wt | 92.4 | 3 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.80× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.3) |
| [[KATO III (line)]] | alt | 63.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.6) | — |
| [[LoVo (line)]] | wt | 24.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.99× (z +12.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 35.6 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +13.0) | — |
| [[NCI-H460 (line)]] | wt | 63.3 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 40.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 32.2 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 51.2 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 39.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +12.3) | — |
| [[C-33 A (line)]] | alt | 29.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.83× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.6) |
| [[Hs 766T (line)]] | wt | 36.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +12.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 73.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 46.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +13.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 30.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.28× (z +16.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 45.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +11.8) ⚠ toxic; transcription drop | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0776× (z -10.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 30.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.09× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 26.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.06× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 30.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +10.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 46.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 22.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.95× (z +14.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 61.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 22.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.46× (z +11.2) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 32.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +10.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 55.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 48.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +10.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 51.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -11.2) |
| [[SW48 (line)]] | wt | 31.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.61× (z +10.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | +0.77 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[SUMO3]] | +0.74 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[AP2M1]] | +0.71 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[FUCA2]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[TMX1]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[CMPK1]] | +0.70 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[BPNT2]] | +0.68 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[PPT1]] | +0.67 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[TWF1]] | +0.67 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[RPN1]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[SCARB2]] | +0.66 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[CRTAP]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF316]] | -0.72 | -0.65 / -0.75 | both halves | 7e-06 |  |
| [[MTRES1]] | -0.70 | -0.55 / -0.67 | both halves | 1e-05 |  |
| [[PPP1R35]] ⚠ | -0.67 | -0.58 / -0.65 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PRPF38B]] | -0.67 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[CROCCP2-1]] | -0.66 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[EIF5B]] | -0.66 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.64 | -0.55 / -0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TARS2]] | -0.63 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[NEMF]] | -0.62 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[NFKBIL1]] | -0.62 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[MRPS18B]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[SURF6]] | -0.62 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[ESF1]] | -0.62 | -0.57 / -0.64 | both halves | 9e-06 |  |
| [[PPIG]] | -0.62 | -0.56 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PGRMC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RBBP7]] | C | RBBP7's natural level strengthens PGRMC1's drug response | RBBP7's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse -0.25; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.769). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-27.5, -21.5); signed map (-21.4, -38.4). **Vector** length 106, 28.3% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +16.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +6.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.9 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | +1.2 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.6 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.6 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.3 | -3.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.2 | -1.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -3.0 | -1.9 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -3.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | progesterone receptor membrane component 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:119,236,245-119,244,466 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HPR6.6 |
| Gene groups (HGNC) | Membrane associated progesterone receptor family; Cytochrome b5 domain containing |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O00264](https://www.uniprot.org/uniprotkb/O00264) (Membrane-associated progesterone receptor component 1):

> Component of a progesterone-binding protein complex. Binds progesterone. Has many reported cellular functions (heme homeostasis, interaction with CYPs). Required for the maintenance of uterine histoarchitecture and normal female reproductive lifespan (By similarity). Intracellular heme chaperone. Regulates heme synthesis via interactions with FECH and acts as a heme donor for at least some hemoproteins. Forms a ternary complex with TMEM97 receptor and low density lipid receptor/LDLR, which …

**Summary**, from NCBI Gene [10857](https://www.ncbi.nlm.nih.gov/gene/10857):

> This gene encodes a putative membrane-associated progesterone steroid receptor. The protein is expressed predominantly in the liver and kidney. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:16090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16090) · Entrez [10857](https://www.ncbi.nlm.nih.gov/gene/10857) · UniProt [O00264](https://www.uniprot.org/uniprotkb/O00264) · Ensembl [ENSG00000101856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101856)

## Data

Gene col 2181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2181); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2181]; `tensor/DDL_lfc|DDL_z.npy` [2181]; `embed/gene_vectors.npy` [2181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2181 or target_col == 2181). Every well: [[PGRMC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGRMC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
