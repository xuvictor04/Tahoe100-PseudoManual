---
symbol: "CTNNA1"
type: "gene"
col: 498
ensembl_id: "ENSG00000044115"
name: "catenin alpha 1"
location: "5q31.2"
module: 119
arm: "+"
pooled_cpm: 550.78
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# CTNNA1

*catenin alpha 1* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.36× (z +7.4, q 8e-11, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.577× (z -12.7, q 2e-34, down in 47 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.729× (z -7.6, q 3e-12, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP1B]] (+0.66, fdr 7e-06), [[YWHAZ]] (+0.63, fdr 7e-06), [[IQGAP1]] (+0.59, fdr 7e-06); moves opposite to [[DDX55]] (-0.60, fdr 1e-05), [[DTWD1]] (-0.56, fdr 1e-05), [[TAB1]] (-0.56, fdr 3e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CLU]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +7.4 | 8e-11 | 32/48 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +5.8 | 2e-06 | 30/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.16× | +4.9 | 2e-04 | 18/48 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.21×** | +4.7 | 4e-04 | 26/48 (SNU-1, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.19× | +3.9 | 0.011 | 19/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.17× | +3.7 | 0.021 | 19/47 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.16× | +3.6 | 0.027 | 17/47 (SNU-1, PANC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.029 | 22/47 (COLO 205, AsPC-1, …) | rises with dose |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.035 | 11/48 (RKO, NCI-H1573, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.11 | 15/47 (NCI-H460, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.12 | 3/48 (LS 180, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.577×** | -12.7 | 2e-34 | 47/47 (RKO, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.700×** | -8.6 | 2e-15 | 36/48 (HOP62, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.704×** | -8.4 | 6e-15 | 35/48 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.708×** | -8.3 | 1e-14 | 37/48 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.729×** | -7.6 | 3e-12 | 38/48 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -6.1 | 8e-08 | 23/48 (RKO, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Amsacrine (drug)]] 5 µM |  | 0.860× | -5.2 | 2e-05 | 14/48 (A549, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.814×** | -4.8 | 1e-04 | 25/48 (A-172, HEC-1-A, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.837× | -4.3 | 0.001 | 22/48 (SW 1271, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.844× | -4.1 | 0.002 | 20/48 (HOP62, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.847× | -4.0 | 0.003 | 20/48 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.856× | -3.8 | 0.008 | 20/48 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.804×** | -3.7 | 0.008 | 31/48 (A-172, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.898× | -3.7 | 0.010 | 1/48 (hTERT-HPNE) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.903× | -3.5 | 0.020 | 10/48 (COLO 205, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.870× | -3.4 | 0.026 | 9/48 (SNU-423, LS 180, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.823×** | -3.3 | 0.026 | 24/47 (NCI-H2347, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.880× | -3.1 | 0.060 | 18/48 (HOP62, SW 900, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.881× | -3.1 | 0.061 | 12/49 (Hs 766T, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.873× | -3.0 | 0.065 | 9/47 (KATO III, AsPC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 812 | 2 (1 ⚠) | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.67× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.515× (z -12.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H1573 (line)]] | alt | 609 | 2 (2 ⚠) | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +19.0) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.551× (z -11.2) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 404 | 5 (3 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.78× (z +12.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.602× (z -10.2) ⚠ toxic |
| [[C32 (line)]] | wt | 578 | 2 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +29.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.369× (z -14.0) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.454× (z -11.5) |
| [[HOP62 (line)]] | alt | 650 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.455× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[Hs 766T (line)]] | wt | 531 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.471× (z -11.3) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 400 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +17.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.493× (z -10.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 562 | 0 | 4 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.497× (z -11.7) ⚠ cell-cycle shift, explains ~12% of this change |
| [[AsPC-1 (line)]] | alt | 629 | 2 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.554× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[CFPAC-1 (line)]] | alt | 852 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.425× (z -12.4) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.465× (z -11.5) |
| [[HT-29 (line)]] | alt | 664 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.423× (z -11.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 410 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.452× (z -14.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW 900 (line)]] | alt | 420 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 5 µM 0.537× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 570 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.465× (z -13.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 345 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 629 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.29× (z +11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 1.92× (z +8.6) | — |
| [[H4 (line)]] | wt | 413 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.80× (z +8.9) | — |
| [[KATO III (line)]] | alt | 675 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.414× (z -13.8) ⚠ toxic |
| [[LS 180 (line)]] | wt | 530 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.67× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.542× (z -10.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[MIA PaCa-2 (line)]] | alt | 444 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.02× (z +11.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.532× (z -9.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 425 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.434× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 682 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.534× (z -11.6) ⚠ toxic |
| [[J82 (line)]] | alt | 455 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.506× (z -12.5) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.612× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 610 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.480× (z -11.8) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 746 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.562× (z -11.1) |
| [[RKO (line)]] | wt | 487 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.292× (z -21.0) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 487 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.414× (z -9.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 671 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.532× (z -11.6) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.630× (z -8.8) |
| [[SW480 (line)]] | alt | 532 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.55× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.512× (z -12.6) ⚠ toxic |
| [[BT-474 (line)]] | alt | 629 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.492× (z -10.9) ⚠ cell-cycle shift, explains ~14% of this change |
| [[HepG2_C3A (line)]] | wt | 616 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 625 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.546× (z -9.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 340 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 512 | 1 (1 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 1.71× (z +8.7) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[Panc 03.27 (line)]] | alt | 631 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.495× (z -9.8) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 857 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.555× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 435 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.76× (z +11.4) | — |
| [[SW48 (line)]] | wt | 444 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 436 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 668 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 347 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 437 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 473 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 563 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 559 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 358 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 435 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 495 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 640 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP1B]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[YWHAZ]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 914 |
| [[IQGAP1]] | +0.59 | +0.60 / +0.66 | both halves | 7e-06 | pathway: Cell-Cell communication; STRING 859 |
| [[SH3KBP1]] | +0.57 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[HAPSTR1]] | +0.56 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[MAP1LC3B]] | +0.56 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[GLS]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[UCHL1]] | +0.54 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[DIAPH1]] | +0.54 | +0.42 / +0.68 | both halves | 4e-05 | pathway: RHO GTPase Effectors |
| [[DYNC1H1]] | +0.53 | +0.44 / +0.58 | both halves | 3e-05 | pathway: RHO GTPase Effectors |
| [[MAP4]] | +0.52 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[DNAJB6]] | +0.51 | +0.50 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX55]] | -0.60 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[DTWD1]] | -0.56 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[TAB1]] | -0.56 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[SETDB1]] | -0.55 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[SCAMP3]] | -0.55 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[RPUSD2]] | -0.55 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[TARS2]] | -0.54 | -0.37 / -0.72 | both halves | 9e-05 |  |
| [[KBTBD6]] | -0.54 | -0.39 / -0.65 | both halves | 5e-05 |  |
| [[GTF3C2]] | -0.53 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[NCBP2AS2]] | -0.53 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[LSM7]] | -0.52 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[COIL]] | -0.52 | -0.42 / -0.63 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLU]] | B | CLU activity lowers CTNNA1's level | lines that do not express CLU (11) vs lines expressing it (39) | 1.36× higher at baseline in the lines without CLU | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MYO5B]] | B | MYO5B activity raises CTNNA1's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 1.25× lower at baseline in the lines without MYO5B | 0.029 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[HDAC6]] | B | HDAC6 activity raises CTNNA1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction -0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.3, -18.5); signed map (-9.5, 34.0). **Vector** length 135, 50.0% of its response variance represented; |z| ≥ 3 in 1,572 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +9.8 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +9.0 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.6 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.9 | +0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.3 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.1 | +3.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.1 | -12.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.5 | -7.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -0.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.9 | -3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.5 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | catenin alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:138,610,967-138,935,034 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAP102 |
| Gene groups (HGNC) | Alpha catenins |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 25 pathways, smallest: CDH11 homotypic and heterotypic interactions; Regulation of CDH19 Expression and Function; Regulation of CDH11 function |
| Matched by | ensembl_id |

**Function**, from UniProt [P35221](https://www.uniprot.org/uniprotkb/P35221) (Catenin alpha-1):

> Associates with the cytoplasmic domain of a variety of cadherins. The association of catenins to cadherins produces a complex which is linked to the actin filament network, and which seems to be of primary importance for cadherins cell-adhesion properties. Can associate with both E- and N-cadherins. Originally believed to be a stable component of E-cadherin/catenin adhesion complexes and to mediate the linkage of cadherins to the actin cytoskeleton at adherens junctions. In contrast, cortical …

**Summary**, from NCBI Gene [1495](https://www.ncbi.nlm.nih.gov/gene/1495):

> This gene encodes a member of the catenin family of proteins that play an important role in cell adhesion process by connecting cadherins located on the plasma membrane to the actin filaments inside the cell. The encoded mechanosensing protein contains three vinculin homology domains and undergoes conformational changes in response to cytoskeletal tension, resulting in the reconfiguration of cadherin-actin filament connections. Certain mutations in this gene cause butterfly-shaped pigment …

**Accessions** — [HGNC:2509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2509) · Entrez [1495](https://www.ncbi.nlm.nih.gov/gene/1495) · UniProt [P35221](https://www.uniprot.org/uniprotkb/P35221) · Ensembl [ENSG00000044115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000044115)

## Data

Gene col 498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 498); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 498]; `tensor/DDL_lfc|DDL_z.npy` [498]; `embed/gene_vectors.npy` [498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 498 or target_col == 498). Every well: [[CTNNA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTNNA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
