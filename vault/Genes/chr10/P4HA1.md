---
symbol: "P4HA1"
type: "gene"
col: 4385
ensembl_id: "ENSG00000122884"
name: "prolyl 4-hydroxylase subunit alpha 1"
location: "10q22.1"
module: 79
arm: "+"
pooled_cpm: 524.4
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# P4HA1

*prolyl 4-hydroxylase subunit alpha 1* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.36× (z +7.2, q 3e-10, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.313× (z -18.4, q 0e+00, down in 46 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.465× (z -17.8, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM3A]] (+0.81, fdr 7e-06), [[HILPDA]] (+0.78, fdr 7e-06), [[WDR45B]] (+0.76, fdr 7e-06); moves opposite to [[COA7]] (-0.62, fdr 1e-05), [[ZBTB45]] (-0.60, fdr 1e-05), [[POGK]] (-0.59, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PLOD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +7.2 | 3e-10 | 42/48 (HEC-1-A, C-33 A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +6.7 | 4e-09 | 35/48 (SK-MEL-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.85×** | +5.3 | 2e-05 | 45/48 (HT-29, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 1e-04 | 36/49 (HEC-1-A, CHP-212, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.014 | 19/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.037 | 37/48 (CFPAC-1, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.060 | 31/49 (HT-29, RPMI-7951, …) | top dose only | plate-row cell shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.21× | +3.2 | 0.11 | 24/48 (NCI-H1792, NCI-H460, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.11 | 21/49 (AsPC-1, MIA PaCa-2, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.14× | +3.1 | 0.11 | 12/48 (HOP62, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4385.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.313×** | -18.4 | 0e+00 | 46/47 (HCT15, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.465×** | -17.8 | 0e+00 | 46/48 (A-172, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.435×** | -13.7 | 1e-40 | 48/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.427×** | -13.5 | 3e-39 | 45/48 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.461×** | -12.3 | 2e-32 | 38/44 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.483×** | -11.1 | 1e-26 | 42/45 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.506×** | -10.8 | 3e-25 | 47/47 (COLO 205, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -10.2 | 1e-22 | 40/49 (SW 900, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.587×** | -8.8 | 1e-16 | 47/48 (SW 900, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.797×** | -3.7 | 0.012 | 27/48 (SW48, LS 180, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.806×** | -3.5 | 0.021 | 30/48 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.799×** | -3.5 | 0.025 | 26/47 (SW48, NCI-H2347, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.811×** | -3.4 | 0.026 | 26/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.804×** | -3.3 | 0.037 | 27/47 (HCT15, CHP-212, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.824×** | -3.1 | 0.086 | 23/48 (NCI-H1573, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 858 | 2 (1 ⚠) | 8 (5 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.71× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -20.7) |
| [[HT-29 (line)]] | alt | 557 | 1 | 9 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.59× (z +9.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.257× (z -18.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.507× (z -13.4) |
| [[HCT15 (line)]] | alt | 968 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -20.0) |
| [[SW 900 (line)]] | alt | 812 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -21.2) |
| [[SW480 (line)]] | alt | 486 | 0 | 9 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.277× (z -18.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.599× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 844 | 0 | 8 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.348× (z -14.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.391× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 845 | 0 | 8 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -18.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -15.8) |
| [[LS 180 (line)]] | wt | 686 | 0 | 8 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.223× (z -17.9) |
| [[NCI-H2347 (line)]] | alt | 600 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -24.2) |
| [[SW48 (line)]] | wt | 843 | 1 | 7 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.50× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.289× (z -12.4) |
| [[A-172 (line)]] | wt | 513 | 3 (1 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.41× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -28.2) |
| [[HEC-1-A (line)]] | alt | 541 | 2 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.81× (z +12.0) | [[Harringtonine (drug)]] 5 µM 0.349× (z -14.5) |
| [[HepG2_C3A (line)]] | wt | 729 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -18.5) |
| [[hTERT-HPNE (line)]] | wt | 766 | 1 | 6 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.16× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -13.4) |
| [[KATO III (line)]] | alt | 403 | 1 | 6 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.50× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -21.9) |
| [[RPMI-7951 (line)]] | alt | 656 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -16.8) |
| [[SK-MEL-2 (line)]] | alt | 350 | 3 (1 ⚠) | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.98× (z +14.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.266× (z -16.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.479× (z -9.6) |
| [[SW1417 (line)]] | alt | 393 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -19.3) |
| [[AsPC-1 (line)]] | alt | 493 | 1 (1 ⚠) | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.326× (z -14.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.542× (z -11.3) |
| [[BT-474 (line)]] | alt | 391 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -14.8) |
| [[Hs 766T (line)]] | wt | 396 | 1 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.1) ⚠ cell-cycle shift, explains ~14% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.313× (z -14.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.622× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 486 | 2 (2 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +13.0) ⚠ cell-cycle shift, explains ~14% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.284× (z -15.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.478× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 297 | 1 (1 ⚠) | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.596× (z -10.1) |
| [[AN3 CA (line)]] | alt | 626 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -25.8) |
| [[CHP-212 (line)]] | wt | 523 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.92× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -17.7) |
| [[COLO 205 (line)]] | alt | 529 | 1 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +8.9) ⚠ cell-cycle shift, explains ~14% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.223× (z -15.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -12.5) |
| [[HOP62 (line)]] | alt | 1,030 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -13.5) |
| [[HS-578T (line)]] | alt | 463 | 2 (1 ⚠) | 3 | [[Panobinostat (drug)]] 0.5 µM 2.42× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -14.7) |
| [[LoVo (line)]] | wt | 464 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.282× (z -16.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.406× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 338 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.439× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 575 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.268× (z -16.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.491× (z -13.4) |
| [[RKO (line)]] | wt | 345 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -15.0) |
| [[A-427 (line)]] | wt | 384 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.611× (z -10.2) |
| [[A549 (line)]] | wt | 354 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -17.5) |
| [[C-33 A (line)]] | alt | 548 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.84× (z +10.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.272× (z -13.1) ⚠ toxic |
| [[C32 (line)]] | wt | 673 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 719 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.362× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 445 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +10.3) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.95× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.282× (z -15.5) |
| [[NCI-H661 (line)]] | alt | 352 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 456 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.4) |
| [[SNU-423 (line)]] | alt | 656 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -20.3) |
| [[A498 (line)]] | wt | 218 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.480× (z -10.9) |
| [[J82 (line)]] | alt | 290 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.340× (z -13.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.493× (z -9.0) |
| [[PANC-1 (line)]] | alt | 482 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.377× (z -12.3) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 204 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.6) |
| [[SNU-1 (line)]] | wt | 376 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.371× (z -11.0) |
| [[SW 1088 (line)]] | alt | 802 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -9.6) |
| [[NCI-H2122 (line)]] | alt | 650 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 630 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 573 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM3A]] | +0.81 | +0.83 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[HILPDA]] | +0.78 | +0.82 / +0.72 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.76 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.76 | +0.79 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[ANKRD37]] | +0.75 | +0.76 / +0.69 | both halves | 7e-06 | STRING 443 |
| [[FAM13A]] | +0.75 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[KDM4B]] | +0.74 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[PIK3C2A]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[MXI1]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[PDK3]] | +0.73 | +0.79 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[SAP30-DT]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COA7]] | -0.62 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[ZBTB45]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[POGK]] | -0.59 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[RAD51D]] | -0.59 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[TMEM147-AS1]] | -0.59 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ZNF839]] | -0.58 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[TXNRD2]] | -0.58 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[POGLUT1]] | -0.58 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[ZNF239]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ZC3H7B]] | -0.57 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[MAPKAPK5]] | -0.57 | -0.52 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLOD2]] | B | PLOD2 activity raises P4HA1's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.29× lower at baseline in the lines without PLOD2 | 0.041 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[ADM]] | B | ADM activity raises P4HA1's level | lines that do not express ADM (6) vs lines expressing it (44) | 1.53× lower at baseline in the lines without ADM | 0.060 | ⚠ within organs, on part of the lines; also absent: FTH1, CDC42EP1, ENSG00000284716; its own permutation p |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers P4HA1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[RAD51D]] | C | RAD51D's natural level weakens P4HA1's drug response | RAD51D's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70, reverse -0.40; direction not clear | 0.012 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.847). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.8, -16.4); signed map (-35.2, 23.5). **Vector** length 172, 65.8% of its response variance represented; |z| ≥ 3 in 1,519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.5 | +7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.8 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.2 | +4.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.7 | +2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.9 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.7 | +5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +2.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.5 | -11.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -10.4 | -13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.9 | -13.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.9 | -10.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -9.7 | -18.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.4 | -3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.5 | -3.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.4 | -2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -2.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | prolyl 4-hydroxylase subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:73,007,217-73,096,974 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C-P4Halpha(I); previously P4HA |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases; Prolyl 4-hydroxylase subunits |
| Hallmark sets | IL2_STAT5_SIGNALING, GLYCOLYSIS, HYPOXIA, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: Maturation of DENV proteins; Collagen biosynthesis and modifying enzymes; Collagen formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P13674](https://www.uniprot.org/uniprotkb/P13674) (Prolyl 4-hydroxylase subunit alpha-1):

> Catalyzes the post-translational formation of 4-hydroxyproline in -Xaa-Pro-Gly- sequences in collagens and other proteins.

**Summary**, from NCBI Gene [5033](https://www.ncbi.nlm.nih.gov/gene/5033):

> This gene encodes a component of prolyl 4-hydroxylase, a key enzyme in collagen synthesis composed of two identical alpha subunits and two beta subunits. The encoded protein is one of several different types of alpha subunits and provides the major part of the catalytic site of the active enzyme. In collagen and related proteins, prolyl 4-hydroxylase catalyzes the formation of 4-hydroxyproline that is essential to the proper three-dimensional folding of newly synthesized procollagen chains. …

**Accessions** — [HGNC:8546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8546) · Entrez [5033](https://www.ncbi.nlm.nih.gov/gene/5033) · UniProt [P13674](https://www.uniprot.org/uniprotkb/P13674) · Ensembl [ENSG00000122884](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122884)

## Data

Gene col 4385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4385); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4385]; `tensor/DDL_lfc|DDL_z.npy` [4385]; `embed/gene_vectors.npy` [4385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4385 or target_col == 4385). Every well: [[P4HA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/P4HA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
