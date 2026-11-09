---
symbol: "TRAF3IP2"
type: "gene"
col: 641
ensembl_id: "ENSG00000056972"
name: "TRAF3 interacting protein 2"
location: "6q21"
module: 94
arm: "+"
pooled_cpm: 26.06
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# TRAF3IP2

*TRAF3 interacting protein 2* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.52× (z +7.9, q 2e-12, up in 25 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.408× (z -16.7, q 0e+00, down in 40 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTN2A3P-1]] (+0.59, fdr 2e-05), [[NEURL3]] (+0.58, fdr 1e-05), [[RIPK2]] (+0.58, fdr 2e-05); moves opposite to [[ADAM10]] (-0.53, fdr 3e-05), [[CNN2]] (-0.49, fdr 7e-05), [[EIF4EBP2]] (-0.49, fdr 4e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RNF144B]] → it (grade B ⚠); 2 go from it, the strongest it → [[KIAA1217]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 641.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.9 | 2e-12 | 25/42 (NCI-H2347, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +7.4 | 3e-11 | 26/45 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.79×** | +5.7 | 3e-06 | 20/46 (HS-578T, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +5.5 | 7e-06 | 19/40 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.8 | 2e-04 | 16/39 (LoVo, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +4.7 | 2e-04 | 18/44 (CFPAC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.27×** | +4.6 | 4e-04 | 18/44 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.26×** | +4.2 | 0.002 | 18/43 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +4.2 | 0.002 | 16/45 (AsPC-1, NCI-H2030, …) | top dose only |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.17× | +4.2 | 0.002 | 15/45 (HS-578T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.073 | 12/45 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.12× | +3.2 | 0.073 | 8/45 (HCT15, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 641.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.408×** | -16.7 | 0e+00 | 40/45 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.467×** | -14.1 | 6e-43 | 37/45 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.492×** | -12.7 | 2e-34 | 23/33 (NCI-H2030, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.524×** | -12.0 | 5e-31 | 27/41 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.587×** | -9.9 | 6e-21 | 27/45 (HS-578T, hTERT-HPNE, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -8.8 | 9e-17 | 27/43 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.736×** | -5.7 | 1e-06 | 23/45 (hTERT-HPNE, BT-474, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.808×** | -5.6 | 2e-06 | 20/45 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.746×** | -5.2 | 9e-06 | 17/45 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.736×** | -5.2 | 9e-06 | 22/37 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.764×** | -4.8 | 9e-05 | 20/43 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.768×** | -4.7 | 1e-04 | 21/44 (SNU-423, SW48, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.769×** | -4.7 | 1e-04 | 20/44 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.796×** | -4.2 | 0.001 | 16/45 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.797×** | -4.2 | 0.001 | 17/44 (HCT15, HS-578T, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.807×** | -4.0 | 0.003 | 16/45 (SNU-423, HS-578T, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.860× | -3.9 | 0.003 | 16/45 (Hs 766T, NCI-H1792, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **0.810×** | -3.8 | 0.005 | 7/45 (LS 180, NCI-H1792, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.818×** | -3.7 | 0.006 | 14/45 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.813×** | -3.7 | 0.007 | 13/45 (hTERT-HPNE, SNU-423, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.819×** | -3.7 | 0.007 | 10/45 (hTERT-HPNE, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 78.0 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.206× (z -11.6) |
| [[hTERT-HPNE (line)]] | wt | 61.0 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.180× (z -12.8) |
| [[HS-578T (line)]] | alt | 46.4 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -13.4) |
| [[A498 (line)]] | wt | 36.0 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.365× (z -9.4) |
| [[BT-474 (line)]] | alt | 22.2 | 3 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 6.55× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~81% of this change |
| [[LoVo (line)]] | wt | 31.2 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 67.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0885× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.198× (z -13.2) |
| [[C32 (line)]] | wt | 57.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -11.4) |
| [[A-172 (line)]] | wt | 15.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -8.8) |
| [[HOP62 (line)]] | alt | 21.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -8.8) |
| [[KATO III (line)]] | alt | 24.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.292× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 26.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0600× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 45.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -11.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW48 (line)]] | wt | 44.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +11.4) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +14.2) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[COLO 205 (line)]] | alt | 30.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -11.1) |
| [[H4 (line)]] | wt | 28.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -9.3) |
| [[HCT15 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 30.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0817× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 24.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[RKO (line)]] | wt | 20.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 30.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.6) |
| [[SHP-77 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SK-MEL-2 (line)]] | alt | 44.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.252× (z -10.8) |
| [[A-427 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN2A3P-1]] | +0.59 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[NEURL3]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[RIPK2]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[BTN2A3P]] | +0.54 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[IL15RA]] | +0.54 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[OTUD7B]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[NINJ1]] | +0.52 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[TATDN3]] | +0.51 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[ADPRM]] | +0.51 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[TEFM]] | +0.51 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[YJU2B]] | +0.50 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[CASP7]] | +0.50 | +0.50 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM10]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[CNN2]] | -0.49 | -0.37 / -0.51 | both halves | 7e-05 |  |
| [[EIF4EBP2]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[RBBP7]] | -0.48 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[STT3B]] | -0.47 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[TBCD]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[GSPT1]] | -0.47 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[SORT1]] | -0.46 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[FAM120A]] | -0.46 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[ARHGAP4]] | -0.46 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[MAPK1]] | -0.45 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[ACTB]] | -0.45 | -0.39 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF144B]] | B | RNF144B activity raises TRAF3IP2's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without RNF144B | 0.025 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[JAK2]] | B | JAK2 activity raises TRAF3IP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[APOL3]] | B | APOL3 activity raises TRAF3IP2's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 2.03× lower at baseline in the lines without APOL3 | 0.064 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[PSMB5]] | B | PSMB5 activity lowers TRAF3IP2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1217]] | C | TRAF3IP2 activity raises KIAA1217's level | lines that do not express TRAF3IP2 (3) vs lines expressing it (47) | 6.61× lower at baseline in the lines without TRAF3IP2 | 0.053 | ⚠ few lines (3 vs 47); across organs; also absent: ARMCX3, SFXN3, HBEGF |
| cells under [[Belumosudil (mesylate) (drug)]] 5 µM | C | TRAF3IP2 activity lowers the cells' numbers under Belumosudil (mesylate) 5 µM (makes them more sensitive) | lines that do not express TRAF3IP2 (3) vs lines expressing it (45) | the lines without TRAF3IP2: 1.35× the cells of the other lines | 0.099 | ⚠ few lines (3 vs 47); across organs; also absent: ARMCX3, SFXN3, HBEGF |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.469). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.1, 1.5); signed map (43.2, 10.9). **Vector** length 96.8, 21.5% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.9 | +5.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.7 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +2.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.2 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +2.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | +0.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~81% of this change | -3.0 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.1 | -4.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | TRAF3 interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:111,555,381-111,606,906 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586G0522, ACT1, CIKS; previously C6orf4, C6orf5, C6orf6, C6orf2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O43734](https://www.uniprot.org/uniprotkb/O43734) (E3 ubiquitin ligase TRAF3IP2):

> E3 ubiquitin ligase that catalyzes 'Lys-63'-linked polyubiquitination of target protein, enhancing protein-protein interaction and cell signaling. Transfers ubiquitin from E2 ubiquitin-conjugating enzyme UBE2V1-UBE2N to substrate protein. Essential adapter molecule in IL17A-mediated signaling. Upon IL17A stimulation, interacts with IL17RA and IL17RC receptor chains through SEFIR domains and catalyzes 'Lys-63'-linked polyubiquitination of TRAF6, leading to TRAF6-mediated activation of NF-kappa-B …

**Summary**, from NCBI Gene [10758](https://www.ncbi.nlm.nih.gov/gene/10758):

> This gene encodes a protein involved in regulating responses to cytokines by members of the Rel/NF-kappaB transcription factor family. These factors play a central role in innate immunity in response to pathogens, inflammatory signals and stress. This gene product interacts with TRAF proteins (tumor necrosis factor receptor-associated factors) and either I-kappaB kinase or MAP kinase to activate either NF-kappaB or Jun kinase. Several alternative transcripts encoding different isoforms have …

**Accessions** — [HGNC:1343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1343) · Entrez [10758](https://www.ncbi.nlm.nih.gov/gene/10758) · UniProt [O43734](https://www.uniprot.org/uniprotkb/O43734) · Ensembl [ENSG00000056972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000056972)

## Data

Gene col 641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 641); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 641]; `tensor/DDL_lfc|DDL_z.npy` [641]; `embed/gene_vectors.npy` [641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 641 or target_col == 641). Every well: [[TRAF3IP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAF3IP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
