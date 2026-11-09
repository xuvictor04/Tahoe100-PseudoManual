---
symbol: "TTL"
type: "gene"
col: 3611
ensembl_id: "ENSG00000114999"
name: "tubulin tyrosine ligase"
location: "2q14.1"
module: 59
arm: "-"
pooled_cpm: 37.91
n_lines_expressing: 48
n_dd_up: 31
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# TTL

*tubulin tyrosine ligase* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.99× (z +16.4, q 0e+00, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.735× (z -5.2, q 1e-04, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GATAD2A]] (+0.68, fdr 7e-06), [[LETM1]] (+0.68, fdr 7e-06), [[LRP8]] (+0.67, fdr 7e-06); moves opposite to [[DBP]] (-0.70, fdr 7e-06), [[CIR1]] (-0.67, fdr 7e-06), [[PPIL4]] (-0.67, fdr 7e-06).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[RFLNB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3611.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +16.4 | 0e+00 | 39/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.08×** | +12.3 | 1e-32 | 37/46 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.00×** | +11.2 | 6e-27 | 34/38 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.90×** | +10.8 | 4e-25 | 36/44 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.87×** | +10.6 | 3e-24 | 39/46 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.84×** | +10.3 | 8e-23 | 36/46 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.72×** | +9.1 | 6e-18 | 33/45 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.71×** | +8.7 | 3e-16 | 31/45 (A498, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +8.6 | 4e-16 | 36/46 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +8.1 | 3e-14 | 35/46 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.56×** | +7.5 | 3e-12 | 36/45 (HEC-1-A, A498, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +7.4 | 6e-12 | 30/46 (NCI-H1792, AsPC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +7.3 | 2e-11 | 29/46 (NCI-H1792, H4, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.56×** | +7.2 | 2e-11 | 29/46 (HT-29, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.57×** | +7.0 | 9e-11 | 26/43 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +6.0 | 6e-08 | 30/45 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +5.5 | 2e-06 | 25/46 (NCI-H1792, RKO, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +5.2 | 7e-06 | 26/46 (NCI-H460, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.34×** | +4.9 | 3e-05 | 22/45 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +4.5 | 1e-04 | 21/46 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +4.4 | 2e-04 | 20/46 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.005 | 15/45 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.009 | 12/45 (NCI-H460, NCI-H1792, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.009 | 15/45 (SW480, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.015 | 16/45 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.028 | 16/45 (NCI-H1792, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3611.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM |  | **0.735×** | -5.2 | 1e-04 | 26/46 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.566×** | -5.0 | 1e-04 | 28/46 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.820×** | -4.8 | 4e-04 | 24/46 (SW48, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.605×** | -4.4 | 0.001 | 21/44 (H4, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.676×** | -3.5 | 0.060 | 18/46 (SNU-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 0.828× | -3.2 | 0.13 | 15/46 (C-33 A, NCI-H2030, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | 0.830× | -3.2 | 0.13 | 14/46 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.825× | -3.1 | 0.13 | 20/46 (A-427, A-172, …) | inconsistent across doses | composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.880× | -3.1 | 0.14 | 7/46 (HCT15, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 36.2 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.09× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 20.3 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 32.0 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 21.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H460 (line)]] | wt | 49.2 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +13.1) | — |
| [[A-427 (line)]] | wt | 70.4 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.252× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 50.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -16.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 37.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 51.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.613× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 31.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.3) | — |
| [[C-33 A (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[C32 (line)]] | wt | 33.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[CHP-212 (line)]] | wt | 59.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0887× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~77% of this change |
| [[HOP62 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.574× (z -13.7) ⚠ position not correctable |
| [[Hs 766T (line)]] | wt | 22.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 29.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +10.9) | — |
| [[LoVo (line)]] | wt | 21.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LOX-IMVI (line)]] | wt | 40.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -16.3) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 17.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 51.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.254× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~77% of this change |
| [[NCI-H23 (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 45.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.69× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 60.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SNU-423 (line)]] | alt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +11.0) | — |
| [[SW1417 (line)]] | alt | 35.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +11.2) | — |
| [[SW48 (line)]] | wt | 60.5 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.212× (z -9.8) |
| [[AN3 CA (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.49 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 60.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[LETM1]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[LRP8]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[SRPK1]] | +0.67 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[NBPF20]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[MACROH2A1]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[FARP1]] | +0.65 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ZNF731P]] | +0.65 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[FAM20B]] | +0.65 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[UGGT2]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBP]] | -0.70 | -0.70 / -0.64 | both halves | 7e-06 |  |
| [[CIR1]] | -0.67 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[PPIL4]] | -0.67 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[AFTPH]] | -0.66 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[KMT2E]] | -0.65 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[SNX2]] | -0.64 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[ASB8]] | -0.63 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[KBTBD7]] | -0.63 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[TCEAL8]] | -0.63 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[SPOP]] | -0.62 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[MYNN]] | -0.62 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[BTN3A1]] | -0.62 | -0.57 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFLNB]] | B | RFLNB activity raises TTL's level | lines that do not express RFLNB (16) vs lines expressing it (34) | 2.04× lower at baseline in the lines without RFLNB | 0.005 | ⚠ within organs, on part of the lines; also absent: FSD1, B4GALNT1, ANTXR1 |
| [[DHRS3]] | B | DHRS3 activity lowers TTL's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.65× higher at baseline in the lines without DHRS3 | 0.039 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[NCS1]] | B | NCS1 activity raises TTL's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without NCS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[SACS]] | B | SACS activity raises TTL's level | lines that do not express SACS (5) vs lines expressing it (45) | 2.54× lower at baseline in the lines without SACS | 0.058 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[DHRS3]] | B | DHRS3 activity strengthens TTL's drug response | lines that do not express DHRS3 (13) vs lines expressing it (33) | the lines without DHRS3 respond 0.47× as strongly (z diff +1.79); strongest at Doxorubicin (hydrochloride) 5 µM: 1.30x vs 1.89x (z diff +2.7) | 0.060 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2; target measured in part of the lines; artifact flags |
| [[GIHCG]] | B | GIHCG activity raises TTL's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 2.09× lower at baseline in the lines without GIHCG | 0.080 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[TNFRSF14]] | B | TNFRSF14 activity lowers TTL's level | lines that do not express TNFRSF14 (12) vs lines expressing it (38) | 1.64× higher at baseline in the lines without TNFRSF14 | 0.082 | ⚠ within organs, on part of the lines; also absent: ZNF785, ZNF69, ENSG00000259345 |
| [[PLXNA2]] | B | PLXNA2 activity lowers TTL's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.59× higher at baseline in the lines without PLXNA2 | 0.085 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[GBX2-AS1]] | B | GBX2-AS1 activity raises TTL's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without GBX2-AS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[MTHFD1L]] | C | MTHFD1L activity raises TTL's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 3.79× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.728). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.9, -35.0); signed map (-19.0, -49.1). **Vector** length 115, 32.0% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.2 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +5.1 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.6 | +10.8 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.6 | +4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.5 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +7.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.4 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.0 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.2 | -4.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.4 | -5.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.0 | -5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.8 | -3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.8 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | tubulin tyrosine ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:112,482,156-112,541,739 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC46235 |
| Gene groups (HGNC) | Tubulin tyrosine ligase family |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NG68](https://www.uniprot.org/uniprotkb/Q8NG68) (Tubulin--tyrosine ligase):

> Catalyzes the post-translational addition of a tyrosine to the C-terminal end of detyrosinated alpha-tubulin.

**Summary**, from NCBI Gene [150465](https://www.ncbi.nlm.nih.gov/gene/150465):

> TTL is a cytosolic enzyme involved in the posttranslational modification of alpha-tubulin (see MIM 602529). Alpha-tubulin within assembled microtubules is detyrosinated over time at the C terminus. After microtubule disassembly, TTL restores the tyrosine residues and consequently participates in a cycle of tubulin detyrosination and tyrosination (Erck et al., 2003 [PubMed 14571137]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:21586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21586) · Entrez [150465](https://www.ncbi.nlm.nih.gov/gene/150465) · UniProt [Q8NG68](https://www.uniprot.org/uniprotkb/Q8NG68) · Ensembl [ENSG00000114999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114999)

## Data

Gene col 3611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3611); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3611]; `tensor/DDL_lfc|DDL_z.npy` [3611]; `embed/gene_vectors.npy` [3611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3611 or target_col == 3611). Every well: [[TTL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
