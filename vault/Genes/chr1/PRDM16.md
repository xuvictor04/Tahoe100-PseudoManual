---
symbol: "PRDM16"
type: "gene"
col: 6635
ensembl_id: "ENSG00000142611"
name: "PR/SET domain 16"
location: "1p36.32"
module: 133
arm: "+"
pooled_cpm: 28.81
n_lines_expressing: 32
n_dd_up: 18
n_dd_down: 19
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# PRDM16

*PR/SET domain 16* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.84× (z +12.9, q 2e-35, up in 16 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.645× (z -9.3, q 1e-17, down in 21 of 30 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC12A7]] (+0.60, fdr 1e-05), [[NIBAN1]] (+0.56, fdr 1e-05), [[HOXB9]] (+0.53, fdr 3e-05); moves opposite to [[UPK1B]] (-0.46, fdr 1e-04), [[SPANXA2-OT1]] (-0.43, fdr 2e-04), [[LDOC1]] (-0.42, fdr 2e-04).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LAMP3]] → it (grade B ⚠); 3 go from it, the strongest it → [[NFATC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6635.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +12.9 | 2e-35 | 16/30 (NCI-H1573, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +8.7 | 1e-15 | 11/30 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.49×** | +6.0 | 5e-07 | 20/30 (C-33 A, SNU-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.5 | 7e-06 | 9/30 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.40×** | +5.0 | 7e-05 | 15/29 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.5 | 7e-04 | 11/30 (BT-474, SW 900, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.21×** | +4.0 | 0.005 | 11/30 (SNU-1, RKO, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.29×** | +4.0 | 0.005 | 13/30 (PANC-1, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.7 | 0.013 | 9/30 (H4, C-33 A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.013 | 9/30 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.014 | 10/30 (C-33 A, H4, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.55×** | +3.4 | 0.025 | 6/26 (NCI-H1573, BT-474, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Encorafenib (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.025 | 9/30 (H4, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.24×** | +3.3 | 0.042 | 9/30 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.24×** | +3.3 | 0.042 | 10/30 (A549, A-427, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.047 | 7/28 (A549, SNU-1, …) | all doses, flat | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.053 | 7/30 (C-33 A, SNU-1, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.053 | 7/30 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.054 | 8/30 (Hs 766T, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.076 | 9/30 (A-427, H4, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6635.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.645×** | -9.3 | 1e-17 | 21/30 (C32, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.638×** | -6.7 | 6e-09 | 14/30 (C32, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.490×** | -5.6 | 5e-06 | 15/30 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.712×** | -5.1 | 5e-05 | 14/28 (SW48, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.720×** | -4.9 | 1e-04 | 13/30 (SNU-1, SW48, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **0.724×** | -4.8 | 1e-04 | 16/28 (SW48, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.738×** | -4.5 | 5e-04 | 17/30 (KATO III, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.752×** | -4.3 | 0.001 | 15/30 (SW480, SNU-1, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.580×** | -4.2 | 0.001 | 13/29 (RKO, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **0.756×** | -4.0 | 0.003 | 13/18 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.606×** | -3.9 | 0.004 | 13/29 (SW480, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **0.693×** | -3.9 | 0.004 | 11/28 (COLO 205, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.776×** | -3.8 | 0.007 | 7/30 (BT-474, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.784×** | -3.6 | 0.012 | 18/30 (MIA PaCa-2, SW1417, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.849× | -3.5 | 0.021 | 5/30 (SW 1271, HepG2/C3A, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **0.793×** | -3.3 | 0.030 | 14/28 (A549, LoVo, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.802×** | -3.2 | 0.048 | 12/30 (Hs 766T, SW480, …) | top dose only | position effect removed |
| [[vincristine (drug)]] 0.05 µM |  | **0.807×** | -3.0 | 0.076 | 5/30 (A-172, SW480, …) | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.815×** | -2.9 | 0.095 | 5/29 (AN3 CA, KATO III, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 127 | 2 | 7 (6 ⚠) | [[Harringtonine (drug)]] 5 µM 2.39× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -8.5) |
| [[SW480 (line)]] | alt | 55.9 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.105× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.409× (z -13.4) |
| [[A-172 (line)]] | wt | 24.5 | 3 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[KATO III (line)]] | alt | 187 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0208× (z -36.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -8.5) |
| [[C32 (line)]] | wt | 26.5 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0674× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.269× (z -10.1) |
| [[RKO (line)]] | wt | 104 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -12.5) |
| [[SNU-1 (line)]] | wt | 101 | 3 (1 ⚠) | 2 (2 ⚠) | [[Artesunate (drug)]] 5 µM 2.61× (z +9.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.57× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[BT-474 (line)]] | alt | 41.0 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +16.6) | [[Selinexor (drug)]] 5 µM 0.424× (z -8.8) |
| [[COLO 205 (line)]] | alt | 72.9 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.128× (z -13.4) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 11.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 39.3× (z +23.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.252× (z -10.8) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 10.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[SW1417 (line)]] | alt | 41.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SW48 (line)]] | wt | 70.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0505× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[A-427 (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[A549 (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 19.3 | 1 | 0 | [[5-Azacytidine (drug)]] 5 µM 5.98× (z +8.5) | — |
| [[H4 (line)]] | wt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[HOP62 (line)]] | alt | 9.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +9.1) | — |
| [[LoVo (line)]] | wt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.65 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.20 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC12A7]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 | same gene group |
| [[NIBAN1]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[HOXB9]] | +0.53 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[BLTP3A]] | +0.53 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[YARS1]] | +0.52 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[CBFA2T3]] | +0.50 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[PCSK6]] | +0.49 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[SLC7A1]] | +0.49 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[SLC22A5]] | +0.49 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[TMEM268]] | +0.48 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[JDP2]] | +0.48 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[CEBPG]] | +0.48 | +0.42 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UPK1B]] | -0.46 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[SPANXA2-OT1]] | -0.43 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[LDOC1]] | -0.42 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[TFPI]] | -0.39 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[SCG3]] | -0.38 | -0.17 / -0.33 | ⚠ not reproduced | 0.001 |  |
| [[PDHB]] | -0.38 | -0.31 / -0.30 | both halves | 2e-04 |  |
| [[NME7]] | -0.38 | -0.28 / -0.33 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMP3]] | B | LAMP3 activity raises PRDM16's level | lines that do not express LAMP3 (18) vs lines expressing it (32) | 2.73× lower at baseline in the lines without LAMP3 | 0.033 | ⚠ within organs, on part of the lines; also absent: OCLN, ENTPD2, LSR |
| [[CBFA2T3]] | B | CBFA2T3 activity raises PRDM16's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 2.36× lower at baseline in the lines without CBFA2T3 | 0.077 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFATC1]] | B | PRDM16 activity raises NFATC1's level | lines that do not express PRDM16 (18) vs lines expressing it (32) | 1.99× lower at baseline in the lines without PRDM16 | 0.006 | ⚠ within organs, on part of the lines; also absent: FBXO2, HAS3, PTPRN2 |
| [[LMF1]] | B | PRDM16 activity raises LMF1's level | lines that do not express PRDM16 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without PRDM16 | 0.040 | ⚠ within organs, on part of the lines; also absent: FBXO2, HAS3, PTPRN2 |
| [[GRID1]] | B | PRDM16 activity raises GRID1's level | lines that do not express PRDM16 (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without PRDM16 | 0.048 | ⚠ within organs, on part of the lines; also absent: FBXO2, HAS3, PTPRN2 |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.1, 47.4); signed map (-12.4, 22.4). **Vector** length 80.0, 18.2% of its response variance represented; |z| ≥ 3 in 864 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +12.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | +3.4 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +3.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.9 | -9.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -2.1 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | PR/SET domain 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:3,069,168-3,438,621 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MEL1, PFM13, KIAA1675, MGC166915, KMT8F |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PR/SET domain family; MicroRNA protein coding host genes; Putative lysine methyltransferases |
| Reactome | 6 pathways, smallest: Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2; PKMTs methylate histone lysines |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAZ2](https://www.uniprot.org/uniprotkb/Q9HAZ2) (Histone-lysine N-methyltransferase PRDM16):

> Transcription regulator that acts both as a histone methyltransferase or chromatin adapter, depending on the context. In the cytoplasm, acts as a histone methyltransferase, which catalyzes monomethylation of 'Lys-9' of free histone H3 (H3K9me1) during translation (By similarity). Monomethylated histone H3 is then transported to the nucleus and incorporated into nucleosomes where SUV39H methyltransferases (SUV39H1 and SUV39H2) use it as a substrate to catalyze histone H3 'Lys-9' trimethylation …

**Summary**, from NCBI Gene [63976](https://www.ncbi.nlm.nih.gov/gene/63976):

> The reciprocal translocation t(1;3)(p36;q21) occurs in a subset of myelodysplastic syndrome (MDS) and acute myeloid leukemia (AML). This gene is located near the 1p36.3 breakpoint and has been shown to be specifically expressed in the t(1:3)(p36,q21)-positive MDS/AML. The protein encoded by this gene is a zinc finger transcription factor and contains an N-terminal PR domain. The translocation results in the overexpression of a truncated version of this protein that lacks the PR domain, which …

**Accessions** — [HGNC:14000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14000) · Entrez [63976](https://www.ncbi.nlm.nih.gov/gene/63976) · UniProt [Q9HAZ2](https://www.uniprot.org/uniprotkb/Q9HAZ2) · Ensembl [ENSG00000142611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142611)

## Data

Gene col 6635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6635); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6635]; `tensor/DDL_lfc|DDL_z.npy` [6635]; `embed/gene_vectors.npy` [6635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6635 or target_col == 6635). Every well: [[PRDM16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDM16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
