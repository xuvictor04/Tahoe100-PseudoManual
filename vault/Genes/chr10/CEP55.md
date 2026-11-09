---
symbol: "CEP55"
type: "gene"
col: 6139
ensembl_id: "ENSG00000138180"
name: "centrosomal protein 55"
location: "10q23.33"
module: 22
arm: "+"
pooled_cpm: 53.9
n_lines_expressing: 48
n_dd_up: 36
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CEP55

*centrosomal protein 55* — 10q23.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (22 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.22× (z +12.2, q 1e-31, up in 37 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.25× (z +4.5, q 2e-04, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.566× (z -8.8, q 1e-15, down in 35 of 46 measured lines) ⚠ cell-cycle shift, explains ~83% of this change. The strongest without an alert is [[Lactate (calcium) (drug)]] 0.5 µM: 0.751× (z -4.4, q 0.001, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BUB1]] (+0.89, fdr 7e-06), [[ARHGAP11A]] (+0.89, fdr 7e-06), [[CCNA2]] (+0.88, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 26 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **2.22×** | +12.2 | 1e-31 | 37/44 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.20×** | +11.7 | 6e-29 | 32/39 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.01×** | +10.7 | 2e-24 | 37/46 (NCI-H460, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.90×** | +9.9 | 7e-21 | 36/46 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.79×** | +8.9 | 5e-17 | 35/46 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | **1.67×** | +7.9 | 3e-13 | 33/44 (HOP62, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +7.1 | 9e-11 | 23/46 (Panc 03.27, RKO, …) | top dose only | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.39×** | +6.9 | 4e-10 | 34/46 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.53×** | +6.5 | 5e-09 | 30/45 (HOP62, SW 900, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +6.1 | 7e-08 | 30/45 (KATO III, A549, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~75% of this change | **1.50×** | +6.0 | 1e-07 | 31/45 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.45×** | +5.7 | 4e-07 | 31/46 (NCI-H2030, HT-29, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **1.46×** | +5.4 | 3e-06 | 23/42 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.41×** | +5.3 | 5e-06 | 26/46 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.25×** | +4.5 | 2e-04 | 22/46 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.34×** | +4.4 | 4e-04 | 23/46 (HT-29, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.33×** | +4.4 | 4e-04 | 25/46 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +4.2 | 9e-04 | 21/46 (A549, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.001 | 18/46 (HOP62, HT-29, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.29×** | +3.9 | 0.002 | 17/46 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.002 | 23/46 (HOP62, SW 900, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **1.58×** | +3.7 | 0.005 | 18/43 (HOP62, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.005 | 21/45 (HOP62, SW 900, …) | rises with dose |  |
| [[vincristine (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.008 | 14/46 (HT-29, SW 900, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.022 | 21/45 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.025 | 15/46 (SW 900, HT-29, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.041 | 14/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +2.9 | 0.051 | 12/46 (HOP62, A549, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +2.9 | 0.051 | 10/46 (RKO, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6139.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.566×** | -8.8 | 1e-15 | 35/46 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.657×** | -8.3 | 3e-14 | 25/46 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.677×** | -6.0 | 4e-07 | 35/46 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.497×** | -5.6 | 3e-06 | 25/40 (A-427, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.667×** | -5.4 | 9e-06 | 26/46 (A-172, LS 180, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.751×** | -4.4 | 0.001 | 24/46 (PANC-1, HS-578T, …) | all doses, flat | position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.678×** | -4.3 | 0.002 | 23/46 (SW480, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.757×** | -4.1 | 0.003 | 22/46 (SW 900, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.815×** | -4.0 | 0.004 | 24/46 (HS-578T, PANC-1, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -3.9 | 0.006 | 1/46 (NCI-H661) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.782×** | -3.8 | 0.008 | 17/46 (SW1417, J82, …) | all doses, flat | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.787×** | -3.7 | 0.011 | 17/46 (SW48, H4, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.771×** | -3.5 | 0.023 | 16/46 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.799×** | -3.4 | 0.023 | 14/46 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **0.803×** | -3.4 | 0.029 | 14/46 (SHP-77, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.753×** | -3.1 | 0.062 | 17/45 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.72 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 61.8 | 2 (2 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | [[Selinexor (drug)]] 5 µM 0.202× (z -19.5) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.369× (z -12.8) |
| [[A-172 (line)]] | wt | 110 | 0 | 7 (5 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.199× (z -14.6) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.337× (z -13.5) |
| [[H4 (line)]] | wt | 44.6 | 0 | 6 (5 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.141× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 46.4 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.223× (z -13.4) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM 0.226× (z -10.0) |
| [[LS 180 (line)]] | wt | 35.0 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.140× (z -14.2) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.249× (z -10.9) |
| [[A-427 (line)]] | wt | 85.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0981× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change |
| [[HOP62 (line)]] | alt | 67.1 | 2 (2 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 2.79× (z +9.1) ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | — |
| [[HT-29 (line)]] | alt | 48.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Docetaxel (drug)]] 0.05 µM 3.38× (z +8.6) ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | [[Bortezomib (drug)]] 5 µM 0.0720× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~48% of this change |
| [[NCI-H460 (line)]] | wt | 46.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.91× (z +8.9) ⚠ cell-cycle shift, explains ~42% of this change | [[Selinexor (drug)]] 5 µM 0.369× (z -10.9) ⚠ cell-cycle shift, explains ~94% of this change |
| [[PANC-1 (line)]] | alt | 96.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[A549 (line)]] | wt | 62.4 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.420× (z -9.1) |
| [[AN3 CA (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 63.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.337× (z -8.5) ⚠ cell-cycle shift, explains ~94% of this change |
| [[LoVo (line)]] | wt | 37.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.397× (z -9.1) ⚠ cell-cycle shift, explains ~94% of this change |
| [[Panc 03.27 (line)]] | alt | 50.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 35.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 38.7 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.165× (z -9.5) |
| [[SNU-1 (line)]] | wt | 50.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 67.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | — |
| [[SW480 (line)]] | alt | 56.7 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.48× (z +8.5) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[AsPC-1 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BUB1]] | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | STRING 928 |
| [[ARHGAP11A]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | STRING 727 |
| [[CCNA2]] | +0.88 | +0.88 / +0.86 | both halves | 7e-06 | STRING 923 |
| [[KIF4A]] | +0.88 | +0.89 / +0.86 | both halves | 7e-06 | STRING 951 |
| [[TPX2]] | +0.88 | +0.88 / +0.88 | both halves | 7e-06 | STRING 944 |
| [[BUB1B]] | +0.88 | +0.86 / +0.88 | both halves | 7e-06 | STRING 939 |
| [[DLGAP5]] | +0.88 | +0.87 / +0.86 | both halves | 7e-06 | STRING 999 |
| [[CIT]] | +0.87 | +0.82 / +0.88 | both halves | 7e-06 | STRING 424 |
| [[KIF23]] | +0.87 | +0.88 / +0.87 | both halves | 7e-06 | STRING 975 |
| [[KNL1]] | +0.87 | +0.85 / +0.86 | both halves | 7e-06 | STRING 611 |
| [[BIRC5]] | +0.87 | +0.85 / +0.88 | both halves | 7e-06 | STRING 913 |
| [[MKI67]] | +0.86 | +0.86 / +0.87 | both halves | 7e-06 | STRING 904 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CEP55's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.25× lower at baseline in the lines without PIMREG | 0.037 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises CEP55's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without MYBL1 | 0.085 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises CEP55's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.02× lower at baseline in the lines without NEURL1B | 0.089 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PBK]] | C | PBK activity raises CEP55's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without PBK | 0.053 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[CDC20]] | C | CDC20 activity raises CEP55's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.21× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SAPCD2]] | C | SAPCD2 activity raises CEP55's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without SAPCD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[AURKB]] | C | AURKB activity raises CEP55's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.36× lower at baseline in the lines without AURKB | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises CEP55's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.03× lower at baseline in the lines without FAM72D | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.896). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.9, -54.8); signed map (-48.5, -42.8). **Vector** length 145, 51.9% of its response variance represented; |z| ≥ 3 in 1,320 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.72 to 60); *DREAM G2/M down* (control, mean cos +0.80 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.69 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | +5.5 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +5.3 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | +5.2 | +12.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.1 | +6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.9 | +10.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +3.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.9 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.0 | +4.4 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +2.8 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -7.3 | -8.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -6.4 | -8.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | -5.6 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.1 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -1.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 55 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.33 — chr10:93,496,612-93,529,092 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10540, CT111; previously C10orf3 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53EZ4](https://www.uniprot.org/uniprotkb/Q53EZ4) (Centrosomal protein of 55 kDa):

> Plays a role in mitotic exit and cytokinesis. Recruits PDCD6IP and TSG101 to midbody during cytokinesis. Required for successful completion of cytokinesis. Not required for microtubule nucleation. Plays a role in the development of the brain and kidney.

**Summary**, from NCBI Gene [55165](https://www.ncbi.nlm.nih.gov/gene/55165):

> Enables identical protein binding activity. Involved in cranial skeletal system development; establishment of protein localization; and midbody abscission. Acts upstream of or within mitotic cytokinesis. Located in Flemming body; centrosome; and cytosol. Implicated in multinucleated neurons, anhydramnios, renal dysplasia, cerebellar hypoplasia and hydranencephaly. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1161) · Entrez [55165](https://www.ncbi.nlm.nih.gov/gene/55165) · UniProt [Q53EZ4](https://www.uniprot.org/uniprotkb/Q53EZ4) · Ensembl [ENSG00000138180](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138180)

## Data

Gene col 6139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6139); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6139]; `tensor/DDL_lfc|DDL_z.npy` [6139]; `embed/gene_vectors.npy` [6139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6139 or target_col == 6139). Every well: [[CEP55 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP55.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
