---
symbol: "RAB3IP"
type: "gene"
col: 4800
ensembl_id: "ENSG00000127328"
name: "RAB3A interacting protein"
location: "12q15"
module: 14
arm: "+"
pooled_cpm: 69.35
n_lines_expressing: 42
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# RAB3IP

*RAB3A interacting protein* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +23.9, q 0e+00, up in 29 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.787× (z -10.0, q 5e-21, down in 21 of 40 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS13A]] (+0.57, fdr 1e-04), [[CD83]] (+0.55, fdr 2e-05), [[SVIP]] (+0.55, fdr 3e-05); moves opposite to [[TMEM11-DT]] (-0.58, fdr 2e-05), [[SLC25A17]] (-0.50, fdr 1e-04), [[HCFC1]] (-0.49, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SAMD12]] → it (grade B ⚠); 5 go from it, the strongest it → [[ATXN1L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +23.9 | 0e+00 | 29/39 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +19.3 | 0e+00 | 32/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +18.3 | 0e+00 | 30/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +17.7 | 0e+00 | 30/40 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +17.6 | 0e+00 | 35/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +14.8 | 0e+00 | 32/40 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +13.9 | 5e-42 | 33/40 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +12.5 | 4e-34 | 31/41 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +8.8 | 6e-17 | 27/40 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +8.7 | 3e-16 | 26/41 (NCI-H460, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.21×** | +5.6 | 1e-06 | 16/41 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.9 | 6e-05 | 19/39 (NCI-H2347, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.7 | 1e-04 | 13/40 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Brivudine (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.006 | 10/41 (NCI-H23, J82, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.012 | 9/40 (HepG2/C3A, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.12× | +3.5 | 0.017 | 7/41 (NCI-H2030, SW48, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.11× | +3.1 | 0.049 | 4/40 (AsPC-1, C-33 A, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.07× | +3.1 | 0.057 | 4/40 (A-427, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4800.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.787×** | -10.0 | 5e-21 | 21/40 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.579×** | -8.1 | 1e-13 | 23/40 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.774×** | -7.6 | 5e-12 | 21/40 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.785×** | -7.2 | 1e-10 | 24/40 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.804×** | -6.5 | 1e-08 | 19/40 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.805×** | -6.4 | 1e-08 | 20/40 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.657×** | -6.3 | 3e-08 | 22/39 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | **0.811×** | -6.0 | 2e-07 | 18/34 (NCI-H23, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -5.6 | 1e-06 | 17/40 (RKO, NCI-H1792, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -5.6 | 1e-06 | 19/41 (NCI-H23, RKO, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.952× | -5.4 | 3e-06 | 0/41 | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.857× | -4.4 | 6e-04 | 19/40 (NCI-H23, RKO, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.911× | -3.9 | 0.004 | 4/40 (NCI-H2347, NCI-H661, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -3.8 | 0.005 | 15/40 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.882× | -3.7 | 0.008 | 9/40 (RKO, NCI-H2347, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.845× | -3.6 | 0.014 | 14/40 (RKO, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.922× | -3.4 | 0.024 | 6/40 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.894× | -3.1 | 0.053 | 9/39 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.928× | -3.1 | 0.053 | 5/40 (Panc 03.27, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 87.4 | 4 | 5 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.87× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.150× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[PANC-1 (line)]] | alt | 41.6 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +19.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 150 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.431× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.513× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 199 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +20.3) | [[Bortezomib (drug)]] 0.05 µM 0.422× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 99.0 | 6 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.77× (z +18.3) | — |
| [[NCI-H1792 (line)]] | alt | 57.3 | 4 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.00× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[NCI-H2030 (line)]] | alt | 27.1 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.41× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[NCI-H2347 (line)]] | alt | 78.4 | 5 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +26.4) | [[NG25 (drug)]] 5 µM 0.248× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 25.6 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 3.70× (z +17.5) | — |
| [[A-172 (line)]] | wt | 30.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +12.6) | — |
| [[A-427 (line)]] | wt | 121 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +11.2) | [[PH-797804 (drug)]] 5 µM 0.223× (z -11.0) |
| [[SW480 (line)]] | alt | 72.6 | 5 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.00× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.92× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 180 | 0 | 4 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.381× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 91.1 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +16.1) | [[Lonafarnib (drug)]] 5 µM 0.149× (z -10.9) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.415× (z -10.1) |
| [[C32 (line)]] | wt | 17.8 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 6.14× (z +9.7) | [[Monocrotaline (drug)]] 0.05 µM 0.166× (z -8.8) |
| [[J82 (line)]] | alt | 87.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.496× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 71.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +12.9) | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[BT-474 (line)]] | alt | 74.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +19.7) | — |
| [[HS-578T (line)]] | alt | 25.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.53× (z +9.6) | — |
| [[KATO III (line)]] | alt | 106 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 83.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.09× (z +8.8) | — |
| [[RKO (line)]] | wt | 257 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 39.9 | 0 | 2 | — | [[Thymol (drug)]] 0.5 µM 0.132× (z -12.4) |
| [[SW1417 (line)]] | alt | 110 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +16.5) | — |
| [[SW48 (line)]] | wt | 70.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.5) | — |
| [[AN3 CA (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0884× (z -8.9) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.0) | — |
| [[C-33 A (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.373× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 65.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +12.1) | — |
| [[HepG2_C3A (line)]] | wt | 72.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +17.3) | — |
| [[hTERT-HPNE (line)]] | wt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0988× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[SNU-423 (line)]] | alt | 43.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +13.0) | — |
| [[SW 900 (line)]] | alt | 38.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.6) | — |
| [[A498 (line)]] | wt | 17.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.78 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 79.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS13A]] | +0.57 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[CD83]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[SVIP]] | +0.55 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[CYRIA]] | +0.55 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[USP2]] | +0.54 | +0.37 / +0.54 | both halves | 9e-05 |  |
| [[N4BP3]] | +0.53 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[TSPAN15]] | +0.52 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[SAMD12]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[TUBB2B]] | +0.50 | +0.34 / +0.48 | both halves | 1e-04 | pathway: Assembly of the 9+0 primary cilium |
| [[SLC9A7]] | +0.50 | +0.42 / +0.40 | both halves | 4e-05 |  |
| [[HMSD]] | +0.49 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[CSRP1]] | +0.48 | +0.40 / +0.44 | both halves | 5e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11-DT]] | -0.58 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[SLC25A17]] | -0.50 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[HCFC1]] | -0.49 | -0.42 / -0.42 | both halves | 4e-05 | pathway: Organelle biogenesis and maintenance |
| [[LRRC41]] | -0.49 | -0.37 / -0.48 | both halves | 9e-05 |  |
| [[PRDM10]] | -0.49 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[FAM185A]] | -0.49 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[GLUD1P3]] | -0.49 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[ACAD9]] | -0.48 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[ADPGK]] | -0.48 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[DUS2]] | -0.47 | -0.22 / -0.43 | both halves | 6e-04 |  |
| [[PRCC]] | -0.47 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[COA6]] | -0.46 | -0.36 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD12]] | B | SAMD12 activity raises RAB3IP's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 3.11× lower at baseline in the lines without SAMD12 | 0.001 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |
| [[ENPP4]] | B | ENPP4 activity raises RAB3IP's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 2.91× lower at baseline in the lines without ENPP4 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[SVIP]] | B | SVIP activity raises RAB3IP's level | lines that do not express SVIP (6) vs lines expressing it (44) | 2.16× lower at baseline in the lines without SVIP | 0.067 | ⚠ within organs, on part of the lines; also absent: PLEKHA5, LRRCC1, USP53; maybe low, not absent; its own permutation p |
| [[CGN]] | B | CGN activity raises RAB3IP's level | lines that do not express CGN (21) vs lines expressing it (29) | 2.96× lower at baseline in the lines without CGN | 0.089 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3; its own permutation p |
| [[RAB11FIP1]] | C | RAB11FIP1 activity raises RAB3IP's level | lines that do not express RAB11FIP1 (3) vs lines expressing it (47) | 3.92× lower at baseline in the lines without RAB11FIP1 | 0.086 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATXN1L]] | B | RAB3IP activity lowers ATXN1L's level | lines that do not express RAB3IP (8) vs lines expressing it (42) | 1.43× higher at baseline in the lines without RAB3IP | 0.039 | ⚠ within organs, on part of the lines; also absent: TBC1D30, CXCL16, ENSG00000288591; maybe low, not absent |
| [[LRRC41]] | B | RAB3IP activity lowers LRRC41's level | lines that do not express RAB3IP (8) vs lines expressing it (42) | 1.25× higher at baseline in the lines without RAB3IP | 0.059 | ⚠ within organs, on part of the lines; also absent: TBC1D30, CXCL16, ENSG00000288591; maybe low, not absent |
| [[PSKH1]] | B | RAB3IP activity lowers PSKH1's level | lines that do not express RAB3IP (8) vs lines expressing it (42) | 1.20× higher at baseline in the lines without RAB3IP | 0.067 | ⚠ within organs, on part of the lines; also absent: TBC1D30, CXCL16, ENSG00000288591; maybe low, not absent |
| [[SVIP]] | B | RAB3IP activity raises SVIP's level | lines that do not express RAB3IP (8) vs lines expressing it (42) | 2.23× lower at baseline in the lines without RAB3IP | 0.072 | ⚠ within organs, on part of the lines; also absent: TBC1D30, CXCL16, ENSG00000288591; maybe low, not absent |
| [[MYO6]] | B | RAB3IP activity raises MYO6's level | lines that do not express RAB3IP (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without RAB3IP | 0.092 | ⚠ within organs, on part of the lines; also absent: TBC1D30, CXCL16, ENSG00000288591; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.393). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.0, 29.1); signed map (-1.3, 20.2). **Vector** length 110, 27.8% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +17.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +12.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +14.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.4 | +13.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.0 | +17.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +8.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +2.8 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -5.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | -5.1 | -4.4 |
|  | [[NG25 (drug)]] 5 µM |  | -4.5 | -8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.1 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -6.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -3.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RAB3A interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:69,738,860-69,823,204 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RABIN3, FLJ22548, RABIN8 |
| Reactome | 11 pathways, smallest: VxPx cargo-targeting to cilium; BBSome-mediated cargo-targeting to cilium; Cargo trafficking to the periciliary membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QF0](https://www.uniprot.org/uniprotkb/Q96QF0) (Rab-3A-interacting protein):

> Guanine nucleotide exchange factor (GEF) which may activate RAB8A and RAB8B. Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form. Mediates the release of GDP from RAB8A and RAB8B but not from RAB3A or RAB5. Modulates actin organization and promotes polarized transport of RAB8A-specific vesicles to the cell surface. Together with RAB11A, RAB8A, the exocyst complex, PARD3, PRKCI, ANXA2, CDC42 and DNMBP promotes transcytosis of PODXL to …

**Summary**, from NCBI Gene [117177](https://www.ncbi.nlm.nih.gov/gene/117177):

> Enables guanyl-nucleotide exchange factor activity and identical protein binding activity. Involved in cilium assembly and protein targeting to membrane. Located in centrosome; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16508) · Entrez [117177](https://www.ncbi.nlm.nih.gov/gene/117177) · UniProt [Q96QF0](https://www.uniprot.org/uniprotkb/Q96QF0) · Ensembl [ENSG00000127328](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127328)

## Data

Gene col 4800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4800); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4800]; `tensor/DDL_lfc|DDL_z.npy` [4800]; `embed/gene_vectors.npy` [4800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4800 or target_col == 4800). Every well: [[RAB3IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB3IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
