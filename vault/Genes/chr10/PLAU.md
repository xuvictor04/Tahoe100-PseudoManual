---
symbol: "PLAU"
type: "gene"
col: 4378
ensembl_id: "ENSG00000122861"
name: "plasminogen activator, urokinase"
location: "10q22.2"
module: 112
arm: "+"
pooled_cpm: 77.91
n_lines_expressing: 24
n_dd_up: 29
n_dd_down: 54
n_dd_up_clean: 14
n_dd_down_clean: 49
in_vector_space: true
direction_upstream: 18
direction_downstream: 22
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# PLAU

*plasminogen activator, urokinase* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.25× (z +14.4, q 2e-44, up in 19 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 5.45× (z +8.8, q 1e-16, up in 21 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 54 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.310× (z -11.7, q 1e-28, down in 22 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF1]] (+0.69, fdr 7e-06), [[CSF2]] (+0.67, fdr 7e-06), [[LIF]] (+0.65, fdr 7e-06); moves opposite to [[TSC22D3]] (-0.58, fdr 9e-06), [[IRAK3]] (-0.55, fdr 1e-05), [[INTS10]] (-0.52, fdr 2e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 22 go from it, the strongest it → [[DUSP10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4378.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.25×** | +14.4 | 2e-44 | 19/22 (SW 900, HOP62, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **4.33×** | +14.0 | 2e-42 | 21/22 (SW 900, HOP62, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.59×** | +11.8 | 9e-30 | 19/20 (SW 900, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +11.0 | 6e-26 | 15/19 (HOP62, SW 900, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **2.12×** | +10.6 | 3e-24 | 20/22 (A549, HOP62, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.45×** | +8.8 | 1e-16 | 21/23 (A549, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **2.20×** | +7.6 | 3e-12 | 15/21 (A549, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.87×** | +6.3 | 3e-08 | 14/21 (HOP62, SW 900, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.15×** | +6.0 | 1e-07 | 14/18 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.69×** | +5.2 | 1e-05 | 16/22 (A549, NCI-H1573, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +5.0 | 2e-05 | 14/23 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.59×** | +4.6 | 2e-04 | 10/22 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 3e-04 | 15/21 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.56×** | +4.3 | 7e-04 | 12/21 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.2 | 9e-04 | 7/21 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.71×** | +3.8 | 0.004 | 14/22 (Panc 03.27, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.005 | 8/23 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.02×** | +3.7 | 0.006 | 14/22 (SW1417, NCI-H2347, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.61×** | +3.4 | 0.019 | 9/22 (H4, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.88×** | +3.3 | 0.024 | 9/20 (CFPAC-1, Panc 03.27, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.58×** | +3.3 | 0.025 | 7/22 (SW1417, PANC-1, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.039 | 13/22 (CFPAC-1, SW 900, …) | rises with dose | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.072 | 6/22 (HOP62, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +2.9 | 0.082 | 0/22 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 5 with an alert ⚠; shown: the 15 strongest. 54 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4378.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.310×** | -11.7 | 1e-28 | 22/22 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.358×** | -10.2 | 3e-22 | 19/22 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.407×** | -8.9 | 7e-17 | 18/22 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.543×** | -6.1 | 2e-07 | 16/22 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.547×** | -6.0 | 2e-07 | 16/22 (NCI-H1573, AsPC-1, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.535×** | -5.8 | 7e-07 | 16/23 (H4, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled); position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.536×** | -5.8 | 7e-07 | 18/21 (NCI-H1573, Panc 03.27, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.564×** | -5.7 | 8e-07 | 18/22 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.565×** | -5.7 | 8e-07 | 18/22 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.685×** | -5.2 | 1e-05 | 12/22 (AsPC-1, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.605×** | -5.0 | 3e-05 | 16/22 (Panc 03.27, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.715×** | -4.7 | 1e-04 | 18/22 (Panc 03.27, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.613×** | -4.7 | 1e-04 | 13/21 (H4, CHP-212, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.628×** | -4.6 | 1e-04 | 17/22 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.630×** | -4.6 | 2e-04 | 20/22 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.76 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 104 | 6 (5 ⚠) | 19 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +16.6) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 31.1× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.0357× (z -17.8) |
| [[H4 (line)]] | wt | 95.2 | 1 (1 ⚠) | 9 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.02× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.130× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 148 | 4 (4 ⚠) | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 8.95× (z +14.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Panobinostat (drug)]] 0.5 µM 0.0955× (z -16.6) |
| [[A549 (line)]] | wt | 80.2 | 7 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +19.4) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 18.9× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 409 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0410× (z -26.0) |
| [[PANC-1 (line)]] | alt | 139 | 5 (4 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 12.8× (z +15.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 18.3× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.0543× (z -18.7) |
| [[HOP62 (line)]] | alt | 37.8 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +19.0) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[SW 900 (line)]] | alt | 76.6 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.62× (z +18.2) ⚠ cell-cycle shift, explains ~70% of this change | — |
| [[AsPC-1 (line)]] | alt | 73.1 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +12.4) ⚠ cell-cycle shift, explains ~70% of this change | [[Panobinostat (drug)]] 0.5 µM 0.0973× (z -14.9) |
| [[Hs 766T (line)]] | wt | 48.1 | 3 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +18.6) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 29.2× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -10.6) |
| [[J82 (line)]] | alt | 58.3 | 2 (2 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 9.20× (z +13.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -11.4) |
| [[SNU-423 (line)]] | alt | 86.6 | 3 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +16.9) ⚠ cell-cycle shift, explains ~70% of this change | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 136 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0682× (z -19.0) |
| [[HS-578T (line)]] | alt | 80.9 | 2 (2 ⚠) | 2 | [[Harringtonine (drug)]] 5 µM 7.11× (z +11.0) ⚠ cell-cycle shift, explains ~30% of this change | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -9.9) |
| [[SW1417 (line)]] | alt | 57.8 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 16.0× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.0998× (z -14.2) |
| [[hTERT-HPNE (line)]] | wt | 65.8 | 2 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 10.9× (z +12.1) ⚠ cell-cycle shift, explains ~30% of this change | [[Triamcinolone (drug)]] 0.5 µM 0.169× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 716 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.4) ⚠ cell-cycle shift, explains ~70% of this change | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 369 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -16.9) |
| [[CHP-212 (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0568× (z -8.8) ⚠ cell-cycle shift, explains ~65% of this change |
| [[RPMI-7951 (line)]] | alt | 54.3 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 10.8× (z +11.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 6.42 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.81 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.88 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.57 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.91 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.95 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.74 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.47 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.77 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF1]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[CSF2]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 446 |
| [[LIF]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[IL23A]] | +0.65 | +0.58 / +0.62 | both halves | 8e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[GATM]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[IFNGR2]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SEMA3A]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[LTB]] | +0.63 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[CD83]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[LINC00973]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CYB5R2]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PRDM8]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | -0.58 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[IRAK3]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[INTS10]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[ACSL1]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PHKA2]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[SAA1]] | -0.49 | -0.57 / -0.43 | both halves | 4e-05 |  |
| [[ZBTB7B]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[VSTM2L]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 7, C 11. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises PLAU's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.7% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HMGN2P46]] | B | HMGN2P46 activity raises PLAU's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 3.22× lower at baseline in the lines without HMGN2P46 | 0.057 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[IL23A]] | B | IL23A activity raises PLAU's level | lines that do not express IL23A (6) vs lines expressing it (44) | 2.99× lower at baseline in the lines without IL23A | 0.076 | ⚠ within organs, on part of the lines; also absent: MYRF; maybe low, not absent |
| [[GJC1]] | B | GJC1 activity raises PLAU's level | lines that do not express GJC1 (13) vs lines expressing it (37) | 2.34× lower at baseline in the lines without GJC1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| [[LAMB3]] | B | LAMB3 activity raises PLAU's level | lines that do not express LAMB3 (22) vs lines expressing it (28) | 2.08× lower at baseline in the lines without LAMB3 | 0.094 | ⚠ within organs, on part of the lines; also absent: KCNK1, LAMC2, PRSS3 |
| [[LAMC2]] | B | LAMC2 activity raises PLAU's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without LAMC2 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[AMIGO2]] | B | AMIGO2 activity raises PLAU's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 3.76× lower at baseline in the lines without AMIGO2 | 0.097 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[TNFRSF9]] | C | TNFRSF9 activity raises PLAU's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 4.24× lower at baseline in the lines without TNFRSF9 | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2; co-absent with the target |
| [[COL22A1]] | C | COL22A1 activity raises PLAU's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.97× lower at baseline in the lines without COL22A1 | 0.031 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[SAA1]] | C | SAA1 activity raises PLAU's level | lines that do not express SAA1 (27) vs lines expressing it (23) | 2.58× lower at baseline in the lines without SAA1 | 0.032 | ⚠ within organs, on part of the lines; also absent: SAA4, MAF, CARD11; co-absent with the target |
| [[G0S2]] | C | G0S2 activity raises PLAU's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 3.72× lower at baseline in the lines without G0S2 | 0.039 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD; co-absent with the target |
| [[CXCL8]] | C | CXCL8 activity raises PLAU's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 2.99× lower at baseline in the lines without CXCL8 | 0.050 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 17, C 5. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP10]] | B | PLAU activity raises DUSP10's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.62× lower at baseline in the lines without PLAU | 0.008 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[SMAD3]] | B | PLAU activity raises SMAD3's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without PLAU | 0.013 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[LAMB3]] | B | PLAU activity raises LAMB3's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.53× lower at baseline in the lines without PLAU | 0.014 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[HMGN2P46]] | B | PLAU activity raises HMGN2P46's level | lines that do not express PLAU (26) vs lines expressing it (24) | 3.05× lower at baseline in the lines without PLAU | 0.025 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[RUNX1]] | B | PLAU activity raises RUNX1's level | lines that do not express PLAU (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without PLAU | 0.031 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[EHD1]] | B | PLAU activity raises EHD1's level | lines that do not express PLAU (26) vs lines expressing it (24) | 1.69× lower at baseline in the lines without PLAU | 0.032 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[FOSL1]] | B | PLAU activity raises FOSL1's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.05× lower at baseline in the lines without PLAU | 0.036 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[LINC00973]] | B | PLAU activity raises LINC00973's level | lines that do not express PLAU (26) vs lines expressing it (24) | 1.71× lower at baseline in the lines without PLAU | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[IL23A]] | B | PLAU activity raises IL23A's level | lines that do not express PLAU (26) vs lines expressing it (24) | 1.50× lower at baseline in the lines without PLAU | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[KIAA1217]] | B | PLAU activity raises KIAA1217's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without PLAU | 0.052 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[LAMC2]] | B | PLAU activity raises LAMC2's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.87× lower at baseline in the lines without PLAU | 0.053 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[SYNJ2]] | B | PLAU activity raises SYNJ2's level | lines that do not express PLAU (26) vs lines expressing it (24) | 1.84× lower at baseline in the lines without PLAU | 0.057 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.0, 2.1); signed map (41.7, 11.2). **Vector** length 107, 33.6% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-10 signaling* (reactome, mean cos +0.56 to 5); *inflammatory response* (hallmark, mean cos +0.51 to 6); *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.56 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +5.1 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +11.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.4 | +14.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | -0.4 |
|  | [[Cyclosporin A (drug)]] 0.5 µM |  | +1.8 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +4.3 |
| fall | [[Triamcinolone (drug)]] 0.5 µM |  | -4.3 | -5.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.2 | -6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | -4.1 | -4.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -4.1 | -2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.0 | -4.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -4.0 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | plasminogen activator, urokinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,909,177-73,917,496 (+) |
| Ensembl biotype | protein_coding |
| Also known as | URK, UPA |
| Gene groups (HGNC) | Serine proteases; Kringle domain containing |
| Hallmark sets | COAGULATION, KRAS_SIGNALING_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: Dissolution of Fibrin Clot; Neutrophil degranulation; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P00749](https://www.uniprot.org/uniprotkb/P00749) (Urokinase-type plasminogen activator):

> Serine protease that cleaves the inactive precursor plasminogen at a specific Arg-Val peptide bond, converting it into active plasmin. Secreted as an inactive zymogen, it is recruited and activated at the cell surface through interaction with the urokinase plasminogen activator receptor (uPAR). Cell-surface activation enables localized, plasmin-dependent pericellular proteolysis, regulating extracellular matrix degradation in cell migration and tissue remodeling. Also contributes to …

**Summary**, from NCBI Gene [5328](https://www.ncbi.nlm.nih.gov/gene/5328):

> This gene encodes a secreted serine protease that converts plasminogen to plasmin. The encoded preproprotein is proteolytically processed to generate A and B polypeptide chains. These chains associate via a single disulfide bond to form the catalytically inactive high molecular weight urokinase-type plasminogen activator (HMW-uPA). HMW-uPA can be further processed into the catalytically active low molecular weight urokinase-type plasminogen activator (LMW-uPA). This low molecular weight form …

**Accessions** — [HGNC:9052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9052) · Entrez [5328](https://www.ncbi.nlm.nih.gov/gene/5328) · UniProt [P00749](https://www.uniprot.org/uniprotkb/P00749) · Ensembl [ENSG00000122861](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122861)

## Data

Gene col 4378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4378); `tables/drug_effects.parquet` (83 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4378]; `tensor/DDL_lfc|DDL_z.npy` [4378]; `embed/gene_vectors.npy` [4378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4378 or target_col == 4378). Every well: [[PLAU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
