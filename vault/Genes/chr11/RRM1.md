---
symbol: "RRM1"
type: "gene"
col: 9453
ensembl_id: "ENSG00000167325"
name: "ribonucleotide reductase catalytic subunit M1"
location: "11p15.4"
module: 6
arm: "+"
pooled_cpm: 65.63
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 11
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# RRM1

*ribonucleotide reductase catalytic subunit M1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.63× (z +17.6, q 0e+00, up in 44 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.63× (z +6.7, q 4e-09, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.656× (z -8.1, q 2e-13, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCI]] (+0.86, fdr 7e-06), [[MMS22L]] (+0.86, fdr 7e-06), [[RFC5]] (+0.86, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DYNC2I2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9453.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **3.63×** | +17.6 | 0e+00 | 44/47 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **3.69×** | +17.1 | 0e+00 | 39/40 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.67×** | +12.4 | 5e-33 | 41/43 (SNU-423, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.63×** | +6.7 | 4e-09 | 37/47 (HOP62, H4, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +5.5 | 4e-06 | 33/47 (H4, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.44×** | +4.8 | 2e-04 | 33/47 (SNU-423, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~92% of this change | **1.41×** | +4.6 | 4e-04 | 28/46 (C32, LoVo, …) | top dose only |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.26×** | +4.5 | 6e-04 | 25/47 (SW48, RKO, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.26×** | +4.4 | 6e-04 | 26/48 (HT-29, SW480, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.26×** | +4.4 | 6e-04 | 29/47 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +4.4 | 6e-04 | 26/47 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.37×** | +4.3 | 9e-04 | 30/47 (A498, HOP62, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.36×** | +4.2 | 1e-03 | 26/47 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.011 | 17/47 (HCT15, HOP62, …) | top dose only |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.28×** | +3.3 | 0.032 | 23/47 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.032 | 22/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.066 | 21/47 (SW480, SNU-1, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.073 | 10/47 (A498, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9453.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.656×** | -8.1 | 2e-13 | 31/47 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.614×** | -6.7 | 8e-09 | 32/47 (A-427, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.765×** | -5.2 | 4e-05 | 34/47 (RKO, HCT15, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.786×** | -4.7 | 4e-04 | 24/47 (HS-578T, A-172, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.813×** | -4.0 | 0.007 | 25/47 (HCT15, RKO, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.655×** | -3.8 | 0.015 | 22/47 (SW480, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.774×** | -3.5 | 0.037 | 25/47 (HCT15, CHP-212, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.776×** | -3.5 | 0.039 | 21/47 (HOP62, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.785×** | -3.3 | 0.058 | 22/47 (A498, H4, …) | all doses, flat |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.696×** | -3.2 | 0.069 | 19/47 (RKO, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.774×** | -3.2 | 0.078 | 21/47 (Hs 766T, RKO, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.795×** | -3.1 | 0.078 | 22/46 (H4, NCI-H460, …) | two highest doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.630×** | -3.1 | 0.078 | 20/47 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~97% of this change | 0.803× | -3.0 | 0.11 | 16/47 (Hs 766T, COLO 205, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.94 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9453. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 97.5 | 3 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | [[Selinexor (drug)]] 5 µM 0.409× (z -13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.428× (z -8.7) |
| [[A-427 (line)]] | wt | 97.0 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -15.7) |
| [[HOP62 (line)]] | alt | 62.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -11.0) |
| [[Hs 766T (line)]] | wt | 56.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 57.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 69.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[SNU-423 (line)]] | alt | 70.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.42× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[H4 (line)]] | wt | 78.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0870× (z -23.0) |
| [[HS-578T (line)]] | alt | 38.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[KATO III (line)]] | alt | 40.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.5) |
| [[LoVo (line)]] | wt | 41.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[NCI-H460 (line)]] | wt | 48.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[PANC-1 (line)]] | alt | 92.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[SW480 (line)]] | alt | 107 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -13.9) |
| [[A-172 (line)]] | wt | 94.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[A549 (line)]] | wt | 48.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.34× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[C32 (line)]] | wt | 34.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.21× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[CFPAC-1 (line)]] | alt | 28.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[HCT15 (line)]] | alt | 96.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 104 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.1) |
| [[HT-29 (line)]] | alt | 57.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 35.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.14× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[LOX-IMVI (line)]] | wt | 52.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.88× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[LS 180 (line)]] | wt | 47.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 28.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.61× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[NCI-H2030 (line)]] | alt | 68.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[Panc 03.27 (line)]] | alt | 36.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[SNU-1 (line)]] | wt | 55.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -9.1) |
| [[AN3 CA (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 26.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.89× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[C-33 A (line)]] | alt | 80.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[J82 (line)]] | alt | 191 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[RPMI-7951 (line)]] | alt | 40.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.70× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 42.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[SW48 (line)]] | wt | 82.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[BT-474 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 99.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9453), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCI]] | +0.86 | +0.84 / +0.87 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[RFC5]] | +0.86 | +0.87 / +0.83 | both halves | 7e-06 | STRING 650 |
| [[POLQ]] | +0.86 | +0.85 / +0.86 | both halves | 7e-06 |  |
| [[WDR76]] | +0.86 | +0.83 / +0.85 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 |  |
| [[EXO1]] | +0.85 | +0.84 / +0.85 | both halves | 7e-06 | STRING 639 |
| [[WDHD1]] | +0.85 | +0.81 / +0.85 | both halves | 7e-06 | STRING 761 |
| [[CENPU]] | +0.85 | +0.84 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[FANCD2]] | +0.85 | +0.82 / +0.87 | both halves | 7e-06 |  |
| [[DTL]] | +0.84 | +0.84 / +0.85 | both halves | 7e-06 | STRING 607 |
| [[CDC45]] | +0.84 | +0.80 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 686 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises RRM1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.19× lower at baseline in the lines without CDC25A | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises RRM1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.58× lower at baseline in the lines without TCF19 | 0.032 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises RRM1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.06× lower at baseline in the lines without E2F8 | 0.049 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises RRM1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.10× lower at baseline in the lines without DSCC1 | 0.056 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises RRM1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.41× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[MCM10]] | C | MCM10 activity raises RRM1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without MCM10 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[PBK]] | C | PBK activity raises RRM1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without PBK | 0.065 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises RRM1's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without ZNF367 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises RRM1's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.73× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.082 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent genes |
| [[PKMYT1]] | C | PKMYT1 activity raises RRM1's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 2.64× lower at baseline in the lines without PKMYT1 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises RRM1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.42× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2I2]] | C | RRM1's natural level strengthens DYNC2I2's drug response | RRM1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.03; direction clear | 0.004 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.891). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.3, -45.8); signed map (-38.2, -43.7). **Vector** length 128, 46.1% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.68 to 65); *DNA strand elongation* (reactome, mean cos +0.72 to 28); *DNA Replication* (reactome, mean cos +0.70 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.4 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.4 | +6.7 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.7 | +4.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.6 | +3.1 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +4.4 | +4.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.6 | +3.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +3.0 | +2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.0 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.8 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -8.1 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -4.1 | -3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.7 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | ribonucleotide reductase catalytic subunit M1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:4,094,707-4,138,932 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ribonucleotide reductase subunits |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P23921](https://www.uniprot.org/uniprotkb/P23921) (Ribonucleoside-diphosphate reductase large subunit):

> Part of the ribonucleotide reductase (RNR) complex composed of a catalytic large alpha subunit (RRM1/RR1) and a small beta subunit, either RRM2/RR2 or RRM2B/RR2B required for DNA synthesis. The active form is an alpha2beta2 heterotetramer in which the RR1-containing subunits (alpha2) catalyze reduction of ribonucleotides to deoxyribonucleotides, while the RRM2-containing subunits (beta2) provide the diferric-tyrosyl radical cofactor required for catalysis and radical transfer. Mechanistically, …

**Summary**, from NCBI Gene [6240](https://www.ncbi.nlm.nih.gov/gene/6240):

> This gene encodes the large and catalytic subunit of ribonucleotide reductase, an enzyme essential for the conversion of ribonucleotides into deoxyribonucleotides. A pool of available deoxyribonucleotides is important for DNA replication during S phase of the cell cycle as well as multiple DNA repair processes. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:10451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10451) · Entrez [6240](https://www.ncbi.nlm.nih.gov/gene/6240) · UniProt [P23921](https://www.uniprot.org/uniprotkb/P23921) · Ensembl [ENSG00000167325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167325)

## Data

Gene col 9453: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9453); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9453, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9453]; `tensor/DDL_lfc|DDL_z.npy` [9453]; `embed/gene_vectors.npy` [9453]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9453 or target_col == 9453). Every well: [[RRM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
