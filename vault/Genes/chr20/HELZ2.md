---
symbol: "HELZ2"
type: "gene"
col: 5086
ensembl_id: "ENSG00000130589"
name: "helicase with zinc finger 2"
location: "20q13.33"
module: 32
arm: "+"
pooled_cpm: 86.3
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 36
n_dd_up_clean: 5
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 61
direction_downstream: 39
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# HELZ2

*helicase with zinc finger 2* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.60× (z +5.4, q 3e-05, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (7 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.416× (z -14.2, q 7e-43, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRF9]] (+0.86, fdr 7e-06), [[ZNFX1]] (+0.85, fdr 7e-06), [[IFI6]] (+0.84, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 61 arrows point to it, the strongest [[SRMS]] → it (grade B ⚠); 39 go from it, the strongest it → [[PML]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.4 | 3e-05 | 29/48 (PANC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +4.6 | 0.001 | 30/48 (NCI-H2347, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.022 | 24/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.58×** | +3.8 | 0.022 | 36/48 (LS 180, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.082 | 26/48 (A498, AsPC-1, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.65× | +3.0 | 0.24 | 21/42 (NCI-H460, A-172, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5086.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.416×** | -14.2 | 7e-43 | 34/49 (SHP-77, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.325×** | -12.4 | 1e-32 | 33/41 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.343×** | -12.2 | 3e-32 | 36/48 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.351×** | -11.5 | 1e-28 | 40/47 (SNU-423, RKO, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.389×** | -10.8 | 4e-25 | 42/48 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.514×** | -10.8 | 5e-25 | 33/49 (C-33 A, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.533×** | -10.2 | 3e-22 | 37/48 (CFPAC-1, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.463×** | -8.8 | 1e-16 | 33/48 (BT-474, SHP-77, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.439×** | -8.7 | 2e-16 | 37/44 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -8.2 | 2e-14 | 37/49 (BT-474, A549, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.505×** | -7.8 | 3e-13 | 34/49 (BT-474, SHP-77, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.546×** | -6.9 | 2e-10 | 41/48 (BT-474, SHP-77, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.329×** | -6.7 | 1e-09 | 34/48 (BT-474, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.602×** | -5.8 | 3e-07 | 30/49 (RPMI-7951, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.606×** | -5.7 | 4e-07 | 30/48 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.602×** | -5.5 | 2e-06 | 32/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.403×** | -5.4 | 2e-06 | 31/49 (A549, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.640×** | -5.1 | 1e-05 | 31/48 (SNU-423, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.645×** | -4.8 | 4e-05 | 32/49 (RKO, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 202 | 0 | 22 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0878× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.261× (z -15.0) |
| [[BT-474 (line)]] | alt | 137 | 0 | 21 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.196× (z -17.4) |
| [[RKO (line)]] | wt | 156 | 0 | 17 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -20.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.303× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 199 | 0 | 15 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.285× (z -16.7) |
| [[SNU-423 (line)]] | alt | 112 | 0 | 15 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0547× (z -21.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.145× (z -14.5) |
| [[LoVo (line)]] | wt | 127 | 0 | 14 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.199× (z -15.6) |
| [[SHP-77 (line)]] | alt | 90.8 | 0 | 14 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0382× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.186× (z -18.2) |
| [[A549 (line)]] | wt | 110 | 0 | 13 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0932× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.317× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 140 | 0 | 13 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0575× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.230× (z -16.8) |
| [[A-172 (line)]] | wt | 139 | 1 | 10 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.74× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0478× (z -27.3) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.305× (z -15.0) |
| [[C-33 A (line)]] | alt | 165 | 0 | 11 (5 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.216× (z -15.3) |
| [[CFPAC-1 (line)]] | alt | 136 | 3 (3 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.354× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 115 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0922× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.397× (z -10.9) |
| [[HS-578T (line)]] | alt | 74.3 | 3 (1 ⚠) | 6 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.20× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.356× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 197 | 1 | 8 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.61× (z +8.5) | [[Tofacitinib (drug)]] 5 µM 0.263× (z -16.9) |
| [[AsPC-1 (line)]] | alt | 183 | 4 (3 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.88× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.458× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 110 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.236× (z -12.9) |
| [[KATO III (line)]] | alt | 116 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.342× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 108 | 0 | 7 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.370× (z -11.6) |
| [[A498 (line)]] | wt | 85.9 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.391× (z -11.6) |
| [[COLO 205 (line)]] | alt | 141 | 0 | 6 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.280× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 76.9 | 4 (3 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 6.13× (z +12.8) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.88× (z +9.9) | [[Tofacitinib (drug)]] 5 µM 0.320× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 101 | 1 (1 ⚠) | 4 | [[Harringtonine (drug)]] 5 µM 4.24× (z +11.0) ⚠ cell-cycle shift, explains ~6% of this change | [[Tofacitinib (drug)]] 5 µM 0.287× (z -13.8) |
| [[Hs 766T (line)]] | wt | 160 | 0 | 4 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.314× (z -13.0) |
| [[A-427 (line)]] | wt | 37.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 23.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.331× (z -8.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 34.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.18× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -9.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 60.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -12.2) |
| [[SW1417 (line)]] | alt | 144 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.5) |
| [[C32 (line)]] | wt | 32.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.92× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 46.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 48.2 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.393× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 50.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.254× (z -9.2) ⚠ toxic |
| [[SW 900 (line)]] | alt | 70.2 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.370× (z -8.5) |
| [[AN3 CA (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 29.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRF9]] | +0.86 | +0.84 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 531 |
| [[ZNFX1]] | +0.85 | +0.79 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 560 |
| [[IFI6]] | +0.84 | +0.77 / +0.87 | both halves | 7e-06 | STRING 553 |
| [[SP110]] | +0.84 | +0.79 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 445 |
| [[IRF7]] | +0.82 | +0.73 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 596 |
| [[BATF2]] | +0.81 | +0.72 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[OAS1]] | +0.81 | +0.72 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 623 |
| [[ISG15]] | +0.80 | +0.73 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 829 |
| [[IFI27]] | +0.80 | +0.71 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 443 |
| [[STAT1]] | +0.79 | +0.79 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 531 |
| [[PARP9]] | +0.79 | +0.74 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 804 |
| [[RIGI]] | +0.79 | +0.75 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 601 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 37, C 24. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRMS]] | B | SRMS activity raises HELZ2's level | lines that do not express SRMS (14) vs lines expressing it (36) | 2.75× lower at baseline in the lines without SRMS | 4e-05 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[OAS2]] | B | OAS2 activity raises HELZ2's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.69× lower at baseline in the lines without OAS2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[OAS1]] | B | OAS1 activity raises HELZ2's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without OAS1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity raises HELZ2's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.77× lower at baseline in the lines without IFI6 | 6e-04 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises HELZ2's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.34× lower at baseline in the lines without MX1 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[BATF2]] | B | BATF2 activity raises HELZ2's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without BATF2 | 0.002 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[IFI27]] | B | IFI27 activity raises HELZ2's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.06× lower at baseline in the lines without IFI27 | 0.003 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[SRMS]] | B | SRMS activity strengthens HELZ2's drug response | lines that do not express SRMS (14) vs lines expressing it (35) | the lines without SRMS respond 0.43× as strongly (z diff +2.99); strongest at Auranofin 5 µM: 0.58x vs 0.32x (z diff +4.6) | 0.004 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2; target measured in part of the lines; artifact flags |
| [[PARP9]] | B | PARP9 activity raises HELZ2's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.85× lower at baseline in the lines without PARP9 | 0.004 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity raises HELZ2's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.70× lower at baseline in the lines without PLSCR1 | 0.006 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises HELZ2's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.33× lower at baseline in the lines without CMPK2 | 0.006 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[ODF3B]] | B | ODF3B activity raises HELZ2's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 1.88× lower at baseline in the lines without ODF3B | 0.008 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 0, C 39. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PML]] | C | HELZ2's natural level strengthens PML's drug response | HELZ2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.86, reverse +0.71; direction not clear | 6e-06 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | HELZ2's natural level strengthens ADAR's drug response | HELZ2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.84, reverse +0.72; direction not clear | 2e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | HELZ2's natural level strengthens IRF9's drug response | HELZ2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.83, reverse +0.75; direction not clear | 3e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | HELZ2's natural level strengthens TDRD7's drug response | HELZ2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.82, reverse +0.60; direction not clear | 5e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM14]] | C | HELZ2's natural level strengthens TRIM14's drug response | HELZ2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.82, reverse +0.80; direction not clear | 8e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | HELZ2's natural level strengthens USP18's drug response | HELZ2's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.82, reverse +0.66; direction not clear | 3e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PNPT1]] | C | HELZ2's natural level strengthens PNPT1's drug response | HELZ2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.78, reverse +0.82; direction not clear | 6e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | HELZ2's natural level strengthens IFIT5's drug response | HELZ2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.73; direction not clear | 7e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SAMHD1]] | C | HELZ2's natural level strengthens SAMHD1's drug response | HELZ2's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.80, reverse +0.66; direction not clear | 7e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | HELZ2's natural level strengthens PARP12's drug response | HELZ2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.75; direction not clear | 0.001 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM25]] | C | HELZ2's natural level strengthens TRIM25's drug response | HELZ2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.73; direction not clear | 0.001 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP14]] | C | HELZ2's natural level strengthens PARP14's drug response | HELZ2's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.64; direction not clear | 0.001 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.803). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.4, 52.4); signed map (65.4, 30.0). **Vector** length 160, 60.1% of its response variance represented; |z| ≥ 3 in 1,586 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.75 to 23); *Interferon Signaling* (reactome, mean cos +0.70 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.73 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.7 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +8.6 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +8.1 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +7.3 | +4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.3 | -0.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +0.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.6 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +3.6 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.5 | +3.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -11.3 | -14.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -10.6 | -6.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -10.0 | -10.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -8.8 | -10.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.1 | -8.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.8 | -7.8 |

## What is on record

|  |  |
|---|---|
| Name | helicase with zinc finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,558,086-63,574,239 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PDIP1, PRIC285, KIAA1769 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; UPF1 like RNA helicases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 20 pathways, smallest: BMAL1:CLOCK,NPAS2 activates circadian expression; RORA,B,C and NR1D1 (REV-ERBA) regulate gene expression; Expression of BMAL (ARNTL), CLOCK, and NPAS2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYK8](https://www.uniprot.org/uniprotkb/Q9BYK8) (3'-5' exoribonuclease HELZ2):

> Multifunctional nuclear protein involved in RNA surveillance, nuclear receptor-mediated transcriptional regulation, and the restriction of mobile genetic elements as part of the innate immune response. Degrades highly structured RNAs through its concerted ATP-dependent RNA helicase and 3' to 5' exoribonuclease activities. Shows a strong preference for pyrimidine over purine residues for its nuclease activity. Acts as a transcriptional coactivator for a number of nuclear receptors including …

**Summary**, from NCBI Gene [85441](https://www.ncbi.nlm.nih.gov/gene/85441):

> The protein encoded by this gene is a nuclear transcriptional co-activator for peroxisome proliferator activated receptor alpha. The encoded protein contains a zinc finger and is a helicase that appears to be part of the peroxisome proliferator activated receptor alpha interacting complex. This gene is a member of the DNA2/NAM7 helicase gene family. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30021) · Entrez [85441](https://www.ncbi.nlm.nih.gov/gene/85441) · UniProt [Q9BYK8](https://www.uniprot.org/uniprotkb/Q9BYK8) · Ensembl [ENSG00000130589](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130589)

## Data

Gene col 5086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5086); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5086]; `tensor/DDL_lfc|DDL_z.npy` [5086]; `embed/gene_vectors.npy` [5086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5086 or target_col == 5086). Every well: [[HELZ2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HELZ2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
