---
symbol: "SPATS2L"
type: "gene"
col: 12138
ensembl_id: "ENSG00000196141"
name: "spermatogenesis associated serine rich 2 like"
location: "2q33.1"
module: 32
arm: "+"
pooled_cpm: 293.11
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 23
n_dd_up_clean: 1
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# SPATS2L

*spermatogenesis associated serine rich 2 like* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.38× (z +9.6, q 3e-19, up in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 6 lines (SW480 2.01×, HEC-1-A 2.01×, RKO 2.41×, NCI-H460 1.75×, …); [[Ixazomib citrate (drug)]] 0.5 µM in 3 lines (J82 1.94×, SW480 1.67×, RKO 2.04×); [[Binimetinib (drug)]] 5 µM in 3 lines (LoVo 1.87×, LS 180 1.80×, Hs 766T 1.78×).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.256× (z -40.3, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP3]] (+0.55, fdr 1e-05), [[SAMD9]] (+0.53, fdr 2e-05), [[LAP3]] (+0.52, fdr 3e-05); moves opposite to [[ARNT]] (-0.50, fdr 1e-04), [[PRPF39]] (-0.46, fdr 4e-04), [[NISCH]] (-0.45, fdr 7e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SERPINB9P1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12138.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 6 lines (SW480 2.01×, HEC-1-A 2.01×, RKO 2.41×, NCI-H460 1.75×, …); [[Ixazomib citrate (drug)]] 0.5 µM in 3 lines (J82 1.94×, SW480 1.67×, RKO 2.04×); [[Binimetinib (drug)]] 5 µM in 3 lines (LoVo 1.87×, LS 180 1.80×, Hs 766T 1.78×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +9.6 | 3e-19 | 30/47 (SW480, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +5.3 | 4e-05 | 23/47 (J82, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.7 | 5e-04 | 22/47 (J82, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +4.2 | 0.004 | 9/47 (HepG2/C3A, COLO 205, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.15× | +4.1 | 0.005 | 20/47 (A549, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.13× | +3.6 | 0.031 | 9/47 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.12× | +3.5 | 0.042 | 10/47 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.11× | +3.0 | 0.16 | 2/47 (C32, Panc 03.27) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12138.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.256×** | -40.3 | 0e+00 | 47/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.282×** | -37.4 | 0e+00 | 47/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.317×** | -34.0 | 0e+00 | 47/47 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.640×** | -18.6 | 0e+00 | 37/47 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.621×** | -14.1 | 8e-43 | 42/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.708×** | -10.2 | 2e-22 | 30/47 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.789×** | -9.9 | 3e-21 | 27/47 (RKO, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.709×** | -9.8 | 1e-20 | 33/46 (SNU-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -9.5 | 1e-19 | 28/47 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.731×** | -9.2 | 2e-18 | 34/47 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.582×** | -8.4 | 3e-15 | 33/48 (A-172, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.759×** | -8.1 | 2e-14 | 32/48 (HOP62, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.833×** | -7.6 | 1e-12 | 22/48 (CFPAC-1, SNU-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.786×** | -6.8 | 3e-10 | 25/47 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.689×** | -5.8 | 3e-07 | 24/47 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.744×** | -4.6 | 1e-04 | 23/47 (AsPC-1, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.746×** | -4.5 | 2e-04 | 22/47 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.748×** | -4.5 | 2e-04 | 24/47 (SNU-1, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12138. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 300 | 0 | 18 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -31.9) |
| [[HEC-1-A (line)]] | alt | 179 | 1 | 9 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.01× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.256× (z -23.7) |
| [[MIA PaCa-2 (line)]] | alt | 425 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -25.8) |
| [[RKO (line)]] | wt | 167 | 4 (2 ⚠) | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.41× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -21.4) |
| [[SW480 (line)]] | alt | 218 | 2 | 8 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.01× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.143× (z -39.1) |
| [[A-172 (line)]] | wt | 328 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -27.8) |
| [[A498 (line)]] | wt | 497 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.233× (z -27.2) |
| [[SNU-1 (line)]] | wt | 805 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -23.1) |
| [[AsPC-1 (line)]] | alt | 521 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.384× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 680 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -28.4) |
| [[Hs 766T (line)]] | wt | 278 | 4 | 4 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 1.95× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.139× (z -28.7) |
| [[NCI-H460 (line)]] | wt | 171 | 1 | 7 (2 ⚠) | [[Auranofin (drug)]] 5 µM 1.75× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.262× (z -25.6) |
| [[J82 (line)]] | alt | 258 | 3 (1 ⚠) | 4 | [[Ixazomib citrate (drug)]] 0.5 µM 1.94× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.270× (z -21.3) |
| [[LoVo (line)]] | wt | 265 | 4 (2 ⚠) | 3 | [[Cobimetinib (drug)]] 5 µM 2.12× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.156× (z -28.8) |
| [[LOX-IMVI (line)]] | wt | 426 | 1 | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.86× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.159× (z -28.5) |
| [[Panc 03.27 (line)]] | alt | 471 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -17.2) |
| [[PANC-1 (line)]] | alt | 440 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -22.9) |
| [[SW1417 (line)]] | alt | 295 | 1 | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.63× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.194× (z -29.2) |
| [[A549 (line)]] | wt | 278 | 1 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.16× (z +12.1) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 5 µM 0.151× (z -29.8) |
| [[SW 900 (line)]] | alt | 323 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -25.3) |
| [[BT-474 (line)]] | alt | 170 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.3) |
| [[COLO 205 (line)]] | alt | 521 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -24.1) |
| [[H4 (line)]] | wt | 202 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -17.9) |
| [[HepG2_C3A (line)]] | wt | 690 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -21.0) |
| [[HS-578T (line)]] | alt | 194 | 1 (1 ⚠) | 4 | [[Harringtonine (drug)]] 0.5 µM 1.91× (z +9.6) ⚠ cell-cycle shift, explains ~18% of this change | [[Panobinostat (drug)]] 5 µM 0.211× (z -23.1) |
| [[KATO III (line)]] | alt | 361 | 1 (1 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.04× (z +9.8) ⚠ cell-cycle shift, explains ~18% of this change | [[Panobinostat (drug)]] 5 µM 0.260× (z -18.5) |
| [[LS 180 (line)]] | wt | 265 | 2 (1 ⚠) | 3 | [[Trametinib (drug)]] 5 µM 1.80× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 5 µM 1.80× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.175× (z -24.5) |
| [[NCI-H1792 (line)]] | alt | 235 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -20.4) |
| [[NCI-H23 (line)]] | alt | 113 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -16.7) |
| [[NCI-H2347 (line)]] | alt | 353 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -21.8) |
| [[SNU-423 (line)]] | alt | 220 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -25.2) |
| [[A-427 (line)]] | wt | 90.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -11.4) |
| [[C32 (line)]] | wt | 139 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.47× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.322× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 169 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +8.8) ⚠ cell-cycle shift, explains ~33% of this change | [[Panobinostat (drug)]] 5 µM 0.260× (z -17.3) |
| [[NCI-H1573 (line)]] | alt | 135 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.8) ⚠ cell-cycle shift, explains ~24% of this change | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 151 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -12.8) |
| [[SW48 (line)]] | wt | 234 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -12.1) |
| [[CHP-212 (line)]] | wt | 161 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -11.8) |
| [[HT-29 (line)]] | alt | 313 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -21.8) |
| [[RPMI-7951 (line)]] | alt | 241 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -13.8) |
| [[SHP-77 (line)]] | alt | 148 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -16.6) |
| [[NCI-H2030 (line)]] | alt | 157 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -18.2) |
| [[HCT15 (line)]] | alt | 127 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -9.0) |
| [[AN3 CA (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 167 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12138), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP3]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SAMD9]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[LAP3]] | +0.52 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[PARP14]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[ZC3HAV1]] | +0.51 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[SAMD9L]] | +0.49 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[NMI]] | +0.47 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[IFIT5]] | +0.47 | +0.39 / +0.46 | both halves | 6e-05 | STRING 510 |
| [[IFIT2]] | +0.47 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[ANO6]] | +0.47 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[TRANK1]] | +0.47 | +0.36 / +0.46 | both halves | 9e-05 |  |
| [[MX2]] | +0.46 | +0.34 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARNT]] | -0.50 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[PRPF39]] | -0.46 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[NISCH]] | -0.45 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[ERICH2]] | -0.44 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[MHENCR]] | -0.43 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[TUT4]] | -0.43 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[RSAD1]] | -0.41 | -0.13 / -0.53 | ⚠ one half (not replicated) | 0.002 |  |
| [[LINC00662]] | -0.41 | -0.24 / -0.43 | both halves | 4e-04 |  |
| [[HEMK1]] | -0.40 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[FHIP1B]] | -0.40 | -0.20 / -0.34 | ⚠ not reproduced | 8e-04 |  |
| [[SAT2]] | -0.40 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[PRPF3]] | -0.40 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[DPM3]] | -0.40 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[MORN4]] | -0.40 | -0.39 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB9P1]] | B | SERPINB9P1 activity raises SPATS2L's level | lines that do not express SERPINB9P1 (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without SERPINB9P1 | 0.010 | ⚠ within organs, on part of the lines; also absent: TINAGL1, MALL, SERPINB9 |
| [[IFIT3]] | B | IFIT3 activity raises SPATS2L's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without IFIT3 | 0.066 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[MX2]] | B | MX2 activity raises SPATS2L's level | lines that do not express MX2 (16) vs lines expressing it (34) | 1.66× lower at baseline in the lines without MX2 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[SLC39A4]] | B | SLC39A4 activity raises SPATS2L's level | lines that do not express SLC39A4 (6) vs lines expressing it (44) | 1.37× lower at baseline in the lines without SLC39A4 | 0.072 | ⚠ within organs, on part of the lines; also absent: LRRC8B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.443). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.9, 55.7); signed map (63.3, 33.7). **Vector** length 121, 38.4% of its response variance represented; |z| ≥ 3 in 1,904 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.8 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.0 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +5.8 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.7 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | -0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +0.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.8 | -9.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.3 | -9.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.7 | -8.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.6 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -10.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.9 | -2.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -3.3 | -2.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated serine rich 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:200,305,881-200,482,264 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DNAPTP6, SGNP |
| Matched by | ensembl_id |

UniProt [Q9NUQ6](https://www.uniprot.org/uniprotkb/Q9NUQ6) carries no function annotation.

**Summary**, from NCBI Gene [26010](https://www.ncbi.nlm.nih.gov/gene/26010):

> Enables RNA binding activity. Located in cytosol and nucleolus. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24574](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24574) · Entrez [26010](https://www.ncbi.nlm.nih.gov/gene/26010) · UniProt [Q9NUQ6](https://www.uniprot.org/uniprotkb/Q9NUQ6) · Ensembl [ENSG00000196141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196141)

## Data

Gene col 12138: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12138); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12138, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12138]; `tensor/DDL_lfc|DDL_z.npy` [12138]; `embed/gene_vectors.npy` [12138]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12138 or target_col == 12138). Every well: [[SPATS2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATS2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
