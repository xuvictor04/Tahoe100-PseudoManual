---
symbol: "IFIT2"
type: "gene"
col: 4136
ensembl_id: "ENSG00000119922"
name: "interferon induced protein with tetratricopeptide repeats 2"
location: "10q23.31"
module: 32
arm: "+"
pooled_cpm: 95.39
n_lines_expressing: 42
n_dd_up: 34
n_dd_down: 28
n_dd_up_clean: 30
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 22
direction_downstream: 48
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFIT2

*interferon induced protein with tetratricopeptide repeats 2* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 5.86× (z +14.6, q 3e-45, up in 39 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.207× (z -13.0, q 9e-36, down in 36 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT3]] (+0.96, fdr 7e-06, ⚠ same locus), [[IFIT1]] (+0.92, fdr 7e-06), [[IFIH1]] (+0.92, fdr 7e-06), [[PARP14]] (+0.90, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[OASL]] → it (grade B ⚠); 48 go from it, the strongest it → [[OASL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4136.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **5.86×** | +14.6 | 3e-45 | 39/40 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **16.4×** | +12.0 | 6e-31 | 38/41 (NCI-H460, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **3.72×** | +10.4 | 4e-23 | 30/40 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.26×** | +9.7 | 3e-20 | 31/40 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **2.07×** | +8.5 | 2e-15 | 26/40 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **2.36×** | +6.8 | 1e-09 | 26/39 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.97×** | +5.6 | 2e-06 | 24/40 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[venetoclax (drug)]] 0.05 µM |  | **2.03×** | +5.5 | 3e-06 | 28/41 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.29×** | +5.1 | 2e-05 | 23/40 (LS 180, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.60×** | +4.5 | 5e-04 | 20/40 (LoVo, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.70×** | +4.3 | 7e-04 | 21/40 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.60×** | +4.3 | 9e-04 | 20/40 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.41×** | +3.9 | 0.004 | 16/41 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.67×** | +3.9 | 0.004 | 16/39 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.004 | 17/40 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.58×** | +3.8 | 0.005 | 19/41 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4136.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.207×** | -13.0 | 9e-36 | 36/40 (SNU-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.218×** | -12.5 | 1e-33 | 40/40 (SNU-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.242×** | -11.7 | 3e-29 | 37/40 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.355×** | -8.5 | 2e-15 | 34/40 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.517×** | -7.7 | 2e-12 | 26/40 (HS-578T, A549, …) | rises with dose | low cells (technical?); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.549×** | -7.0 | 3e-10 | 27/41 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.440×** | -6.7 | 1e-09 | 28/40 (SNU-423, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.441×** | -6.7 | 1e-09 | 27/40 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.476×** | -6.1 | 7e-08 | 25/40 (Panc 03.27, SW 1271, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.534×** | -5.2 | 1e-05 | 25/40 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.556×** | -4.8 | 7e-05 | 22/40 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.569×** | -4.5 | 4e-04 | 21/39 (A-172, Panc 03.27, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.588×** | -4.4 | 5e-04 | 21/39 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.687×** | -4.4 | 5e-04 | 20/41 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.365×** | -4.3 | 5e-04 | 22/41 (SNU-423, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.601×** | -4.2 | 0.001 | 22/41 (SNU-423, HS-578T, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.626×** | -3.8 | 0.004 | 19/40 (BT-474, SNU-423, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **0.438×** | -3.5 | 0.012 | 16/38 (Panc 03.27, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -3.4 | 0.016 | 20/40 (A549, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4136. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 239 | 7 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +22.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 24.5× (z +19.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.168× (z -10.8) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.176× (z -10.5) |
| [[LS 180 (line)]] | wt | 127 | 9 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +20.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 17.1× (z +15.2) | [[Auranofin (drug)]] 5 µM 0.181× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 60.3 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +21.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 16.9× (z +16.7) | [[Panobinostat (drug)]] 0.5 µM 0.216× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 126 | 3 | 3 | [[Harringtonine (drug)]] 0.5 µM 9.95× (z +11.4) | [[Tofacitinib (drug)]] 5 µM 0.219× (z -10.7) |
| [[SNU-423 (line)]] | alt | 243 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0419× (z -12.1) |
| [[A-172 (line)]] | wt | 341 | 1 | 4 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 6.33× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.0863× (z -11.3) |
| [[LoVo (line)]] | wt | 32.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +12.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.35× (z +11.0) | — |
| [[A498 (line)]] | wt | 155 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0826× (z -11.8) |
| [[BT-474 (line)]] | alt | 84.8 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0620× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 189 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 12.3× (z +10.4) | [[Tofacitinib (drug)]] 5 µM 0.167× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 109 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.0× (z +19.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 35.5× (z +14.6) | — |
| [[COLO 205 (line)]] | alt | 150 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.106× (z -9.6) |
| [[HCT15 (line)]] | alt | 46.3 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +12.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 21.9× (z +8.5) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0487× (z -8.7) |
| [[Hs 766T (line)]] | wt | 287 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 26.3× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.160× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 89.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0638× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 227 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 166 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 34.2× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.218× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 82.0 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 86.4× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.0809× (z -9.8) |
| [[SNU-1 (line)]] | wt | 111 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0631× (z -15.2) |
| [[A549 (line)]] | wt | 73.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.132× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0607× (z -9.5) |
| [[H4 (line)]] | wt | 171 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +8.5) ⚠ cell-cycle shift, explains ~43% of this change | [[Belinostat (drug)]] 5 µM 0.0811× (z -9.0) |
| [[HOP62 (line)]] | alt | 38.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +12.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 24.1× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 76.8 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.121× (z -10.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0670× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 131 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.61× (z +12.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.5× (z +9.3) | — |
| [[J82 (line)]] | alt | 49.4 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 11.3× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 35.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.43× (z +10.0) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[HT-29 (line)]] | alt | 83.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +10.5) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1792 (line)]] | alt | 65.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -11.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW 1088 (line)]] | alt | 162 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0608× (z -8.8) |
| [[A-427 (line)]] | wt | 6.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.4 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.56 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4136), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT3]] | +0.96 | +0.96 / +0.95 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999; ⚠ same locus (18.0 kb, same strand: neighbours can correlate without regulation) |
| [[IFIT1]] | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 982 |
| [[IFIH1]] | +0.92 | +0.89 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 976 |
| [[PARP14]] | +0.90 | +0.85 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 740 |
| [[RSAD2]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 962 |
| [[OASL]] | +0.90 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 963 |
| [[RIGI]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 982 |
| [[TRANK1]] | +0.88 | +0.87 / +0.86 | both halves | 7e-06 | same gene group |
| [[XAF1]] | +0.87 | +0.82 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 887 |
| [[DDX60]] | +0.87 | +0.82 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 899 |
| [[SAMD9]] | +0.87 | +0.83 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 781 |
| [[SAMD9L]] | +0.86 | +0.78 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 853 |
| [[HERC5]] | +0.85 | +0.85 / +0.89 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 937 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 14, C 8. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OASL]] | B | OASL activity raises IFIT2's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.25× lower at baseline in the lines without OASL | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[PLAAT4]] | B | PLAAT4 activity raises IFIT2's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 3.21× lower at baseline in the lines without PLAAT4 | 0.006 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[CASP10]] | B | CASP10 activity raises IFIT2's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.20× lower at baseline in the lines without CASP10 | 0.009 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[LMO2]] | B | LMO2 activity raises IFIT2's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 2.74× lower at baseline in the lines without LMO2 | 0.017 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[CXCL10]] | B | CXCL10 activity raises IFIT2's level | lines that do not express CXCL10 (23) vs lines expressing it (27) | 2.61× lower at baseline in the lines without CXCL10 | 0.017 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent |
| [[GBP5]] | B | GBP5 activity raises IFIT2's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.74× lower at baseline in the lines without GBP5 | 0.036 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[IFI16]] | B | IFI16 activity raises IFIT2's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.66× lower at baseline in the lines without IFI16 | 0.041 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[CTSS]] | B | CTSS activity raises IFIT2's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.40× lower at baseline in the lines without CTSS | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[NLRC5]] | B | NLRC5 activity raises IFIT2's level | lines that do not express NLRC5 (5) vs lines expressing it (45) | 3.12× lower at baseline in the lines without NLRC5 | 0.055 | ⚠ within organs, on part of the lines; also absent: NDRG1, APOL6, S100A13; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises IFIT2's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.41× lower at baseline in the lines without RSAD2 | 0.066 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[CFB]] | B | CFB activity raises IFIT2's level | lines that do not express CFB (20) vs lines expressing it (30) | 2.37× lower at baseline in the lines without CFB | 0.067 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[KYNU]] | B | KYNU activity raises IFIT2's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.30× lower at baseline in the lines without KYNU | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 42, C 6. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OASL]] | B | IFIT2 activity raises OASL's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 3.83× lower at baseline in the lines without IFIT2 | 0.005 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[B2M]] | B | IFIT2 activity raises B2M's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 2.53× lower at baseline in the lines without IFIT2 | 0.007 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[GBP3]] | B | IFIT2 activity raises GBP3's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 4.03× lower at baseline in the lines without IFIT2 | 0.008 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[PLAAT4]] | B | IFIT2 activity raises PLAAT4's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 3.15× lower at baseline in the lines without IFIT2 | 0.012 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[MB21D2]] | B | IFIT2 activity raises MB21D2's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 2.50× lower at baseline in the lines without IFIT2 | 0.012 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[GBP4]] | B | IFIT2 activity raises GBP4's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 5.16× lower at baseline in the lines without IFIT2 | 0.014 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[CASP10]] | B | IFIT2 activity raises CASP10's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 2.89× lower at baseline in the lines without IFIT2 | 0.018 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[APOL6]] | B | IFIT2 activity raises APOL6's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 2.70× lower at baseline in the lines without IFIT2 | 0.026 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[FNIP2]] | B | IFIT2 activity raises FNIP2's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without IFIT2 | 0.026 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[IFI44]] | B | IFIT2 activity raises IFI44's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 4.25× lower at baseline in the lines without IFIT2 | 0.027 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[ZC3HAV1]] | B | IFIT2 activity raises ZC3HAV1's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without IFIT2 | 0.034 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[TNFSF10]] | B | IFIT2 activity raises TNFSF10's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 3.12× lower at baseline in the lines without IFIT2 | 0.035 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.895). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.4, 53.3); signed map (63.5, 31.4). **Vector** length 150, 49.3% of its response variance represented; |z| ≥ 3 in 1,326 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.72 to 17); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.77 to 10); *ISG15 antiviral mechanism* (reactome, mean cos +0.79 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.2 | +14.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.8 | +9.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +10.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +8.0 | +12.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +6.6 | +8.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.3 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.7 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.7 | +4.3 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -6.9 | -4.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.4 | -2.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -6.2 | -3.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.7 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.6 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | interferon induced protein with tetratricopeptide repeats 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:89,283,694-89,309,271 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IFI-54, ISG-54K, ISG-54, cig42, GARG-39; previously IFI54, G10P2 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 6 pathways, smallest: Viral strategies to evade IFIT action; IFIT antiviral response; Interferon alpha/beta signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P09913](https://www.uniprot.org/uniprotkb/P09913) (Interferon-induced protein with tetratricopeptide repeats 2):

> IFN-induced antiviral protein which inhibits expression of viral messenger RNAs lacking 2'-O-methylation of the 5' cap. The ribose 2'-O-methylation would provide a molecular signature to distinguish between self and non-self mRNAs by the host during viral infection. Viruses evolved several ways to evade this restriction system such as encoding their own 2'-O-methylase for their mRNAs or by stealing host cap containing the 2'-O-methylation (cap snatching mechanism). Binds AU-rich viral RNAs, …

**Summary**, from NCBI Gene [3433](https://www.ncbi.nlm.nih.gov/gene/3433):

> Enables RNA binding activity. Involved in positive regulation of apoptotic process and response to virus. Acts upstream of or within antiviral innate immune response. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:5409](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5409) · Entrez [3433](https://www.ncbi.nlm.nih.gov/gene/3433) · UniProt [P09913](https://www.uniprot.org/uniprotkb/P09913) · Ensembl [ENSG00000119922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119922)

## Data

Gene col 4136: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4136); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4136, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4136]; `tensor/DDL_lfc|DDL_z.npy` [4136]; `embed/gene_vectors.npy` [4136]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4136 or target_col == 4136). Every well: [[IFIT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFIT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
