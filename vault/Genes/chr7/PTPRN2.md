---
symbol: "PTPRN2"
type: "gene"
col: 7868
ensembl_id: "ENSG00000155093"
name: "protein tyrosine phosphatase receptor type N2"
location: "7q36.3"
module: 141
arm: "+"
pooled_cpm: 131.63
n_lines_expressing: 33
n_dd_up: 23
n_dd_down: 19
n_dd_up_clean: 20
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# PTPRN2

*protein tyrosine phosphatase receptor type N2* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.32× (z +45.8, q 0e+00, up in 28 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.678× (z -6.6, q 3e-08, down in 23 of 30 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.729× (z -5.5, q 9e-06, down in 22 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00460]] (+0.67, fdr 7e-06), [[TRNP1]] (+0.64, fdr 1e-05), [[EFNB2]] (+0.63, fdr 7e-06); moves opposite to [[DNASE2]] (-0.56, fdr 1e-05), [[ASB7]] (-0.53, fdr 1e-05), [[ZNF148]] (-0.52, fdr 3e-05).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CD163L1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7868.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.32×** | +45.8 | 0e+00 | 28/31 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.83×** | +22.7 | 0e+00 | 24/31 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.22×** | +20.6 | 0e+00 | 24/31 (A-172, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.14×** | +20.1 | 0e+00 | 27/31 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.23×** | +14.1 | 7e-43 | 24/31 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +12.4 | 4e-33 | 21/31 (PANC-1, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +10.6 | 3e-24 | 23/31 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +9.4 | 3e-19 | 21/31 (LoVo, C-33 A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +8.2 | 2e-14 | 17/31 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.5 | 6e-09 | 11/32 (RKO, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +5.1 | 2e-05 | 15/31 (HS-578T, H4, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.9 | 4e-05 | 13/32 (BT-474, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.31×** | +4.8 | 8e-05 | 14/31 (H4, HS-578T, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.6 | 2e-04 | 7/28 (C-33 A, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 2e-04 | 11/31 (AsPC-1, HS-578T, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.001 | 13/31 (HS-578T, AsPC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.004 | 14/31 (AsPC-1, HS-578T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7868.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.678×** | -6.6 | 3e-08 | 23/30 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.729×** | -5.5 | 9e-06 | 22/31 (A549, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.751×** | -5.0 | 1e-04 | 18/31 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -4.8 | 2e-04 | 20/31 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.830×** | -4.6 | 4e-04 | 16/31 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.770×** | -4.6 | 5e-04 | 14/31 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -4.4 | 8e-04 | 13/31 (LOX-IMVI, KATO III, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.838× | -4.3 | 0.001 | 13/31 (SW480, HOP62, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.631×** | -4.2 | 0.002 | 16/31 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.794×** | -4.0 | 0.003 | 14/32 (SW480, LOX-IMVI, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.794×** | -3.7 | 0.009 | 11/31 (SW480, HOP62, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.666×** | -3.7 | 0.009 | 17/30 (HepG2/C3A, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.803×** | -3.7 | 0.010 | 19/33 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.670×** | -3.7 | 0.010 | 17/31 (HepG2/C3A, H4, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.676×** | -3.6 | 0.012 | 12/31 (NCI-H460, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.815×** | -3.6 | 0.012 | 17/31 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.871× | -3.3 | 0.023 | 11/32 (SW480, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.864× | -3.2 | 0.033 | 12/32 (SW480, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.870× | -3.1 | 0.048 | 13/31 (SW480, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7868. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 550 | 0 | 16 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -15.2) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.367× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 328 | 11 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +17.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.360× (z -9.6) ⚠ toxic |
| [[H4 (line)]] | wt | 83.7 | 8 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.1) | [[Lonafarnib (drug)]] 5 µM 0.0617× (z -10.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 318 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.291× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 116 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +26.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.326× (z -9.0) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 33.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +38.4) | — |
| [[COLO 205 (line)]] | alt | 52.6 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +18.4) | [[Binimetinib (drug)]] 5 µM 0.167× (z -9.7) |
| [[HS-578T (line)]] | alt | 48.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +27.2) | — |
| [[LoVo (line)]] | wt | 95.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.69× (z +26.2) | — |
| [[LS 180 (line)]] | wt | 82.9 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +14.8) | [[Ixazomib citrate (drug)]] 5 µM 0.334× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 303 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -15.6) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -9.6) |
| [[A-172 (line)]] | wt | 90.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.5× (z +43.5) | — |
| [[NCI-H1573 (line)]] | alt | 162 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +20.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.240× (z -11.0) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 154 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.393× (z -9.7) |
| [[SW 900 (line)]] | alt | 51.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.96× (z +25.0) | — |
| [[SW48 (line)]] | wt | 136 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 32.4× (z +34.5) | [[Digitoxin (drug)]] 5 µM 0.269× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 49.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +26.0) | [[Adagrasib (drug)]] 0.05 µM 0.663× (z -9.8) ⚠ position not correctable |
| [[SW1417 (line)]] | alt | 1,018 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -18.5) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.509× (z -9.2) |
| [[KATO III (line)]] | alt | 385 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -10.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 67.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.9) | [[Trametinib (drug)]] 5 µM 0.218× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.266× (z -9.3) |
| [[RKO (line)]] | wt | 61.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +14.1) | [[Digitoxin (drug)]] 5 µM 0.318× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 46.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.51× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -9.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 141 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +15.3) | [[Ixazomib citrate (drug)]] 5 µM 0.191× (z -10.6) |
| [[C-33 A (line)]] | alt | 51.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +12.1) | — |
| [[SHP-77 (line)]] | alt | 330 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 56.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +17.8) | — |
| [[BT-474 (line)]] | alt | 297 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 33.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +15.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.4) | — |
| [[SW 1088 (line)]] | alt | 95.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.49× (z +10.6) | — |
| [[A498 (line)]] | wt | 23.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.6 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 24.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 27.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 21.2 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 25.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.8 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 24.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 27.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7868), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00460]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[TRNP1]] | +0.64 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[EFNB2]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[PLEC]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 | same gene group |
| [[EGR1]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[EGR3]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[ZFP36]] | +0.58 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[SYNE3]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ASTL]] | +0.57 | +0.60 / +0.49 | both halves | 2e-05 |  |
| [[LINC00659]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[LINC02320]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[SH2D3A]] | +0.56 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNASE2]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ASB7]] | -0.53 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ZNF148]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[CIAO2A]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[GAPVD1]] | -0.50 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[BMPR1A]] | -0.49 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[NDUFAF7]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD163L1]] | B | CD163L1 activity raises PTPRN2's level | lines that do not express CD163L1 (24) vs lines expressing it (26) | 2.13× lower at baseline in the lines without CD163L1 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, ENSG00000230647, CNRIP1; maybe low, not absent |
| [[EGR2]] | B | EGR2 activity raises PTPRN2's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without EGR2 | 0.029 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DIO3OS]] | B | DIO3OS activity raises PTPRN2's level | lines that do not express DIO3OS (25) vs lines expressing it (25) | 2.33× lower at baseline in the lines without DIO3OS | 0.067 | ⚠ within organs, on part of the lines; also absent: NPSR1-AS1, ENSG00000258919, TOX3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.4, 2.1); signed map (7.3, 35.9). **Vector** length 109, 27.0% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +45.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +20.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +12.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.1 | +4.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.8 | +4.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.7 | +3.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.3 | -5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.0 | -6.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type N2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:157,539,056-158,587,823 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0387, phogrin, ICAAR, IA-2beta |
| Gene groups (HGNC) | Protein tyrosine phosphatases receptor type; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92932](https://www.uniprot.org/uniprotkb/Q92932) (Receptor-type tyrosine-protein phosphatase N2):

> Plays a role in vesicle-mediated secretory processes. Required for normal accumulation of secretory vesicles in hippocampus, pituitary and pancreatic islets. Required for the accumulation of normal levels of insulin-containing vesicles and preventing their degradation. Plays a role in insulin secretion in response to glucose stimuli. Required for normal accumulation of the neurotransmitters norepinephrine, dopamine and serotonin in the brain. In females, but not in males, required for normal …

**Summary**, from NCBI Gene [5799](https://www.ncbi.nlm.nih.gov/gene/5799):

> This gene encodes a protein with sequence similarity to receptor-like protein tyrosine phosphatases. However, tyrosine phosphatase activity has not been experimentally validated for this protein. Studies of the rat ortholog suggest that the encoded protein may instead function as a phosphatidylinositol phosphatase with the ability to dephosphorylate phosphatidylinositol 3-phosphate and phosphatidylinositol 4,5-diphosphate, and this function may be involved in the regulation of insulin …

**Accessions** — [HGNC:9677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9677) · Entrez [5799](https://www.ncbi.nlm.nih.gov/gene/5799) · UniProt [Q92932](https://www.uniprot.org/uniprotkb/Q92932) · Ensembl [ENSG00000155093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155093)

## Data

Gene col 7868: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7868); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7868, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7868]; `tensor/DDL_lfc|DDL_z.npy` [7868]; `embed/gene_vectors.npy` [7868]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7868 or target_col == 7868). Every well: [[PTPRN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
