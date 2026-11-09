---
symbol: "BTBD9"
type: "gene"
col: 11461
ensembl_id: "ENSG00000183826"
name: "BTB domain containing 9"
location: "6p21.2"
module: 56
arm: "+"
pooled_cpm: 258.03
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 30
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# BTBD9

*BTB domain containing 9* — 6p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.34× (z +6.2, q 4e-07, up in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.27× (z +5.3, q 3e-05, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.393× (z -29.2, q 0e+00, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.432× (z -26.3, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC6B]] (+0.65, fdr 1e-05), [[TVP23C]] (+0.60, fdr 1e-05), [[HSPA5]] (+0.56, fdr 2e-05); moves opposite to [[CENPL]] (-0.55, fdr 3e-05), [[ARID1A]] (-0.54, fdr 4e-05), [[ZBTB2]] (-0.54, fdr 8e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11461.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.34×** | +6.2 | 4e-07 | 37/47 (H4, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +5.3 | 3e-05 | 30/47 (RKO, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.59×** | +4.8 | 3e-04 | 35/49 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.20× | +4.0 | 0.009 | 20/48 (LoVo, NCI-H2030, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.013 | 27/50 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.013 | 24/48 (Panc 03.27, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.055 | 24/49 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.15× | +3.0 | 0.17 | 14/49 (SW480, LS 180, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.17 | 15/47 (HepG2/C3A, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 26 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11461.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.393×** | -29.2 | 0e+00 | 42/48 (COLO 205, CFPAC-1, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.432×** | -26.3 | 0e+00 | 47/49 (CFPAC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.339×** | -23.0 | 0e+00 | 45/48 (NCI-H1792, COLO 205, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.404×** | -19.3 | 0e+00 | 39/44 (SW48, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.405×** | -19.2 | 0e+00 | 46/47 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.437×** | -18.3 | 0e+00 | 46/49 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.496×** | -15.5 | 0e+00 | 41/48 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.476×** | -15.2 | 0e+00 | 41/45 (CFPAC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.537×** | -13.2 | 5e-38 | 37/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.576×** | -12.2 | 2e-32 | 41/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.610×** | -10.5 | 3e-24 | 42/50 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.612×** | -10.5 | 6e-24 | 35/47 (A-172, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.624×** | -10.4 | 8e-24 | 42/48 (SW480, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **0.641×** | -9.8 | 3e-21 | 42/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **0.424×** | -8.9 | 3e-17 | 42/49 (SNU-423, CFPAC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.793×** | -7.3 | 1e-11 | 31/48 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.756×** | -6.2 | 2e-08 | 27/48 (SW480, NCI-H23, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.588×** | -5.5 | 1e-06 | 29/48 (RPMI-7951, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.694×** | -3.8 | 0.003 | 23/48 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.845× | -3.6 | 0.007 | 19/49 (AsPC-1, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.722×** | -3.4 | 0.014 | 22/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.859× | -3.2 | 0.022 | 16/49 (SNU-423, NCI-H2030, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.870× | -3.1 | 0.034 | 18/48 (AsPC-1, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.875× | -3.0 | 0.049 | 17/48 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Rosiglitazone (drug)]] 5 µM |  | 0.872× | -2.9 | 0.052 | 8/47 (C-33 A, AsPC-1, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.877× | -2.9 | 0.053 | 17/48 (AsPC-1, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11461. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 381 | 0 | 19 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -41.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -33.7) |
| [[SW480 (line)]] | alt | 228 | 0 | 19 (15 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -24.6) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -22.1) |
| [[SNU-423 (line)]] | alt | 322 | 0 | 18 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -29.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -26.1) |
| [[HT-29 (line)]] | alt | 388 | 0 | 16 (13 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.120× (z -21.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 173 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -30.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.245× (z -18.9) |
| [[RPMI-7951 (line)]] | alt | 252 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -22.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -20.5) |
| [[HOP62 (line)]] | alt | 404 | 0 | 14 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -20.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -18.7) |
| [[HS-578T (line)]] | alt | 287 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -32.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -23.0) |
| [[C32 (line)]] | wt | 250 | 1 | 12 (9 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.35× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -31.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -20.9) |
| [[LoVo (line)]] | wt | 400 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -20.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.247× (z -15.9) |
| [[MIA PaCa-2 (line)]] | alt | 197 | 1 | 12 (8 ⚠) | [[Auranofin (drug)]] 5 µM 2.46× (z +11.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.189× (z -20.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.289× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 197 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -27.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -21.0) |
| [[COLO 205 (line)]] | alt | 1,882 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -41.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -25.3) |
| [[A-172 (line)]] | wt | 167 | 0 | 11 (7 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.233× (z -19.2) |
| [[NCI-H1792 (line)]] | alt | 324 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -30.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.106× (z -29.2) |
| [[LS 180 (line)]] | wt | 427 | 0 | 10 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0950× (z -17.6) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -11.9) |
| [[RKO (line)]] | wt | 390 | 1 | 9 (7 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.07× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.176× (z -19.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -18.3) |
| [[SW 900 (line)]] | alt | 253 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -20.9) |
| [[SW48 (line)]] | wt | 281 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0290× (z -33.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -13.1) |
| [[KATO III (line)]] | alt | 406 | 0 | 9 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.199× (z -16.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 298 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -25.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -19.0) |
| [[PANC-1 (line)]] | alt | 145 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -20.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.281× (z -15.3) |
| [[SW1417 (line)]] | alt | 173 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -17.9) |
| [[Hs 766T (line)]] | wt | 206 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -16.1) |
| [[J82 (line)]] | alt | 156 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -21.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.298× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 121 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -25.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.252× (z -18.5) |
| [[HCT15 (line)]] | alt | 440 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 219 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -14.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.437× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 158 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -23.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -18.4) |
| [[NCI-H23 (line)]] | alt | 283 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -27.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -12.9) |
| [[NCI-H2347 (line)]] | alt | 243 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -23.3) |
| [[SNU-1 (line)]] | wt | 353 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.539× (z -10.7) |
| [[A549 (line)]] | wt | 144 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -18.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.315× (z -13.7) |
| [[BT-474 (line)]] | alt | 215 | 1 | 5 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.03× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 222 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -19.2) |
| [[A498 (line)]] | wt | 69.4 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.254× (z -15.7) |
| [[AN3 CA (line)]] | alt | 284 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -11.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.365× (z -8.9) |
| [[H4 (line)]] | wt | 203 | 1 (1 ⚠) | 3 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.42× (z +8.6) ⚠ cell-cycle shift, explains ~35% of this change | [[Harringtonine (drug)]] 5 µM 0.354× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 164 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -12.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -11.1) |
| [[C-33 A (line)]] | alt | 217 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.442× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 154 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -18.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.256× (z -13.6) |
| [[CHP-212 (line)]] | wt | 162 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 176 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -11.5) |
| [[NCI-H596 (line)]] | alt | 301 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.309× (z -9.7) ⚠ transcription drop |
| [[SW 1088 (line)]] | alt | 273 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -10.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 182 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 320 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 194 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11461), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC6B]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[TVP23C]] | +0.60 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[HSPA5]] | +0.56 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[KLC3]] | +0.55 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[RPLP0P2]] | +0.54 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[PRKCZ]] | +0.54 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[GAB2]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[COG5]] | +0.53 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[PIGH]] | +0.53 | +0.51 / +0.36 | both halves | 1e-04 |  |
| [[RPS6KC1]] | +0.52 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[MACO1]] | +0.52 | +0.65 / +0.35 | both halves | 1e-04 |  |
| [[UBE2B]] | +0.52 | +0.43 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPL]] | -0.55 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[ARID1A]] | -0.54 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[ZBTB2]] | -0.54 | -0.58 / -0.37 | both halves | 8e-05 | same gene group |
| [[FAM111A]] | -0.52 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[HNRNPF]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[PATZ1]] | -0.50 | -0.37 / -0.51 | both halves | 8e-05 | same gene group |
| [[MMD]] | -0.49 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[HDGF]] | -0.49 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[BCL9L]] | -0.49 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[ZNF253]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RPRD1B]] | -0.49 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[ARHGEF17]] | -0.48 | -0.45 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BTBD9's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MTOR]] | B | MTOR activity lowers BTBD9's level | compounds that target MTOR: 3 of 8 raise it (Bimiralisib, GSK1059615, Sapanisertib) | 38% of the class's compounds vs 1.4% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[TMCC3]] | B | TMCC3 activity raises BTBD9's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 1.22× lower at baseline in the lines without TMCC3 | 0.082 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.399). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.4, -33.5); signed map (-56.0, 16.9). **Vector** length 95.0, 35.1% of its response variance represented; |z| ≥ 3 in 1,681 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.6 | -5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.6 | -5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.5 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | -6.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.2 | +0.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.2 | -8.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.6 | -13.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -5.5 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -3.2 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.1 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.0 | -2.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | BTB domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.2 — chr6:38,168,451-38,640,148 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1880, dJ322I12.1 |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q96Q07](https://www.uniprot.org/uniprotkb/Q96Q07) carries no function annotation.

**Summary**, from NCBI Gene [114781](https://www.ncbi.nlm.nih.gov/gene/114781):

> This locus encodes a BTB/POZ domain-containing protein. This domain is known to be involved in protein-protein interactions. Polymorphisms at this locus have been reported to be associated with susceptibility to Restless Legs Syndrome and may also be associated with Tourette Syndrome. Alternatively spliced transcript variants have been described. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:21228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21228) · Entrez [114781](https://www.ncbi.nlm.nih.gov/gene/114781) · UniProt [Q96Q07](https://www.uniprot.org/uniprotkb/Q96Q07) · Ensembl [ENSG00000183826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183826)

## Data

Gene col 11461: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11461); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11461, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11461]; `tensor/DDL_lfc|DDL_z.npy` [11461]; `embed/gene_vectors.npy` [11461]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11461 or target_col == 11461). Every well: [[BTBD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTBD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
