---
symbol: "IFT88"
type: "gene"
col: 407
ensembl_id: "ENSG00000032742"
name: "intraflagellar transport 88"
location: "13q12.11"
module: 64
arm: "+"
pooled_cpm: 57.63
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# IFT88

*intraflagellar transport 88* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.55× (z +11.6, q 4e-28, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.519× (z -11.7, q 4e-29, down in 37 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.477× (z -7.2, q 2e-10, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC26]] (+0.61, fdr 1e-05), [[KIF3B]] (+0.57, fdr 1e-05), [[NPHP1]] (+0.56, fdr 3e-05); moves opposite to [[EEF1AKMT3]] (-0.55, fdr 1e-05), [[SEPTIN7P13]] (-0.50, fdr 2e-05), [[DERL1]] (-0.50, fdr 2e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 407.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +11.6 | 4e-28 | 33/48 (NCI-H23, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +11.3 | 3e-27 | 38/48 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.81×** | +11.0 | 5e-26 | 41/48 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +9.5 | 2e-19 | 39/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +6.6 | 3e-09 | 31/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +6.0 | 3e-07 | 29/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +5.6 | 1e-06 | 29/48 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +5.2 | 2e-05 | 27/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.5 | 4e-04 | 24/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +4.3 | 1e-03 | 26/48 (RKO, A498, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.024 | 14/49 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.1 | 0.085 | 18/48 (NCI-H23, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.18× | +3.1 | 0.092 | 15/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.10 | 6/48 (HEC-1-A, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 407.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.519×** | -11.7 | 4e-29 | 37/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.477×** | -7.2 | 2e-10 | 39/49 (H4, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.706×** | -6.5 | 2e-08 | 29/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.726×** | -5.9 | 4e-07 | 27/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.731×** | -5.8 | 7e-07 | 26/48 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.803×** | -5.8 | 8e-07 | 27/48 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.572×** | -5.4 | 4e-06 | 26/44 (Panc 03.27, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.748×** | -5.4 | 5e-06 | 31/48 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.750×** | -5.3 | 6e-06 | 25/48 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.822×** | -5.1 | 1e-05 | 26/49 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.608×** | -4.8 | 7e-05 | 24/48 (HEC-1-A, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.771×** | -4.8 | 7e-05 | 24/47 (NCI-H460, NCI-H23, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **0.788×** | -4.4 | 4e-04 | 25/47 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.791×** | -4.3 | 6e-04 | 23/48 (SW 1088, NCI-H23, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -4.3 | 6e-04 | 23/50 (HEC-1-A, A-427, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.645×** | -4.3 | 7e-04 | 22/48 (C32, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | 0.837× | -3.3 | 0.027 | 13/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.832×** | -3.3 | 0.028 | 17/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.883× | -3.2 | 0.029 | 4/49 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.834× | -3.2 | 0.029 | 16/47 (NCI-H1573, MIA PaCa-2, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 407. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 99.8 | 4 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.411× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.447× (z -11.9) |
| [[NCI-H460 (line)]] | wt | 57.3 | 0 | 8 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.216× (z -15.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.332× (z -11.8) |
| [[A-427 (line)]] | wt | 74.7 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.8) |
| [[HOP62 (line)]] | alt | 80.5 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -17.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -10.8) |
| [[J82 (line)]] | alt | 36.3 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +9.0) | [[Digitoxin (drug)]] 0.5 µM 0.294× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 54.6 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.33× (z +12.9) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -10.4) |
| [[HT-29 (line)]] | alt | 90.9 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -8.8) |
| [[KATO III (line)]] | alt | 62.0 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.29× (z +12.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.404× (z -9.4) ⚠ toxic |
| [[LoVo (line)]] | wt | 49.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +12.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.441× (z -8.9) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 99.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +18.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.356× (z -11.5) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 55.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.7) | — |
| [[A498 (line)]] | wt | 33.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.82× (z +12.5) | — |
| [[C-33 A (line)]] | alt | 115 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.226× (z -14.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -8.6) |
| [[C32 (line)]] | wt | 78.6 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0744× (z -12.8) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.101× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 59.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +11.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.302× (z -9.5) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.353× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 26.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +15.7) | — |
| [[COLO 205 (line)]] | alt | 195 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[HCT15 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.277× (z -11.8) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 36.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 22.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +11.8) | — |
| [[SK-MEL-2 (line)]] | alt | 57.2 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -9.2) |
| [[A-172 (line)]] | wt | 55.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.161× (z -10.9) ⚠ toxic |
| [[H4 (line)]] | wt | 52.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.233× (z -9.3) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 61.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0856× (z -10.5) ⚠ toxic |
| [[LS 180 (line)]] | wt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0856× (z -16.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 43.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +11.7) | — |
| [[SHP-77 (line)]] | alt | 85.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.202× (z -15.4) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 44.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 43.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -8.7) |
| [[SW 1271 (line)]] | alt | 48.6 | 0 | 1 | — | [[Posaconazole (drug)]] 0.5 µM 0.0553× (z -9.8) |
| [[SW 900 (line)]] | alt | 48.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 40.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.9) | — |
| [[A549 (line)]] | wt | 80.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 407), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC26]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 | same gene group; pathway: Assembly of the 9+0 primary cilium; STRING 997 |
| [[KIF3B]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 865 |
| [[NPHP1]] | +0.56 | +0.49 / +0.46 | both halves | 3e-05 | pathway: HALLMARK_SPERMATOGENESIS; STRING 722 |
| [[POLM]] | +0.55 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[METTL23]] | +0.54 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[BBS1]] | +0.54 | +0.63 / +0.48 | both halves | 2e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 845 |
| [[MICU2]] | +0.54 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[DNAL4]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[IFT22]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 | same gene group; pathway: Assembly of the 9+0 primary cilium; STRING 995 |
| [[THG1L]] | +0.53 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[CEP290]] | +0.53 | +0.48 / +0.54 | both halves | 2e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 810 |
| [[CCDC113]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1AKMT3]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[SEPTIN7P13]] | -0.50 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[DERL1]] | -0.50 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[PCGF5]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SLC44A3-AS1]] | -0.49 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[MOCOS]] | -0.49 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[MFAP3L]] | -0.48 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[SPX]] | -0.48 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[CHST7]] | -0.48 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[SMG1P7]] | -0.48 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[MTRR]] | -0.47 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[EPB41L4B]] | -0.46 | -0.57 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers IFT88's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.271). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-32.5, -1.5); signed map (-14.1, -27.1). **Vector** length 112, 31.9% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.0 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.1 | -5.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Resveratrol (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.3 | -11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.7 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 88 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:20,567,138-20,691,444 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hTg737, Tg737, D13S1056E, MGC26259; previously TTC10 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; IFT-B1 complex |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 12 pathways, smallest: Chaperone Mediated Autophagy; Late endosomal microautophagy; Aggrephagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13099](https://www.uniprot.org/uniprotkb/Q13099) (Intraflagellar transport protein 88 homolog):

> Positively regulates primary cilium biogenesis. Also involved in autophagy since it is required for trafficking of ATG16L and the expansion of the autophagic compartment.

**Summary**, from NCBI Gene [8100](https://www.ncbi.nlm.nih.gov/gene/8100):

> This gene encodes a member of the tetratrico peptide repeat (TPR) family. The encoded protein is involved in cilium biogenesis. Mutations of a similar gene in mouse can cause polycystic kidney disease. Several transcript variants encoding distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:20606](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20606) · Entrez [8100](https://www.ncbi.nlm.nih.gov/gene/8100) · UniProt [Q13099](https://www.uniprot.org/uniprotkb/Q13099) · Ensembl [ENSG00000032742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000032742)

## Data

Gene col 407: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 407); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 407, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 407]; `tensor/DDL_lfc|DDL_z.npy` [407]; `embed/gene_vectors.npy` [407]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 407 or target_col == 407). Every well: [[IFT88 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFT88.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
