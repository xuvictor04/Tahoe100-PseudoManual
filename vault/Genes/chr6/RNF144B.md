---
symbol: "RNF144B"
type: "gene"
col: 6007
ensembl_id: "ENSG00000137393"
name: "ring finger protein 144B"
location: "6p22.3"
module: 14
arm: "+"
pooled_cpm: 17.29
n_lines_expressing: 35
n_dd_up: 29
n_dd_down: 29
n_dd_up_clean: 26
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 4
direction_downstream: 15
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# RNF144B

*ring finger protein 144B* — 6p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 10.3× (z +18.2, q 0e+00, up in 26 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.547× (z -9.0, q 1e-16, down in 20 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFNAR2]] (+0.55, fdr 1e-05), [[RIPK2]] (+0.54, fdr 1e-05), [[RTN4RL2]] (+0.54, fdr 1e-05); moves opposite to [[TRBC2]] (-0.48, fdr 6e-05), [[PCNT]] (-0.46, fdr 1e-04), [[ANKMY1]] (-0.46, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[IL15]] → it (grade B ⚠); 15 go from it, the strongest it → [[TSPAN33]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **10.3×** | +18.2 | 0e+00 | 26/32 (J82, BT-474, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +12.0 | 2e-30 | 20/33 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +7.7 | 3e-12 | 17/32 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.66×** | +7.6 | 3e-12 | 14/29 (BT-474, hTERT-HPNE, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +7.6 | 4e-12 | 21/30 (HT-29, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +7.2 | 7e-11 | 13/33 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.46×** | +6.5 | 8e-09 | 18/33 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +6.0 | 1e-07 | 10/32 (NCI-H2347, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +5.7 | 6e-07 | 12/32 (CFPAC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.46×** | +5.7 | 6e-07 | 11/33 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +5.3 | 7e-06 | 14/33 (HT-29, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +4.6 | 2e-04 | 13/31 (HT-29, SNU-423, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.80×** | +4.6 | 2e-04 | 10/32 (NCI-H2347, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.001 | 11/33 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.001 | 8/33 (hTERT-HPNE, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6007.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.547×** | -9.0 | 1e-16 | 20/33 (H4, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -8.3 | 3e-14 | 19/32 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -7.0 | 6e-10 | 19/32 (SNU-423, J82, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.635×** | -6.8 | 2e-09 | 18/33 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.664×** | -6.1 | 1e-07 | 16/31 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.674×** | -5.9 | 4e-07 | 17/32 (SNU-423, J82, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.698×** | -5.4 | 7e-06 | 14/32 (J82, NCI-H1792, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -5.3 | 8e-06 | 14/30 (SK-MEL-2, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.705×** | -5.2 | 1e-05 | 17/30 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.732×** | -4.6 | 2e-04 | 18/27 (SNU-423, LS 180, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.736×** | -4.4 | 6e-04 | 14/19 (A498, CFPAC-1, …) | rises with dose | composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.814×** | -4.3 | 7e-04 | 13/33 (HT-29, Hs 766T, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.758×** | -4.1 | 0.002 | 9/33 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.750×** | -4.1 | 0.002 | 14/30 (SNU-423, J82, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.927× | -4.0 | 0.002 | 3/33 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.603×** | -3.9 | 0.003 | 12/30 (SNU-423, H4, …) | top dose only | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.773×** | -3.8 | 0.004 | 8/33 (SW 1271, NCI-H460, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.787×** | -3.6 | 0.011 | 11/33 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.783×** | -3.5 | 0.014 | 9/32 (HT-29, H4, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.809×** | -3.1 | 0.040 | 12/31 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.809×** | -3.1 | 0.040 | 10/33 (CHP-212, A498, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.811×** | -3.1 | 0.043 | 4/33 (J82, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 146 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 15.7× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -13.8) |
| [[SNU-423 (line)]] | alt | 81.0 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.9× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -16.5) |
| [[A498 (line)]] | wt | 45.5 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.0540× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 11.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.0589× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[NCI-H460 (line)]] | wt | 12.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 16.6× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[A549 (line)]] | wt | 14.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -9.3) |
| [[BT-474 (line)]] | alt | 54.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 31.6× (z +9.7) | — |
| [[H4 (line)]] | wt | 16.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0197× (z -13.4) |
| [[HepG2_C3A (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.181× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 41.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -8.5) |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0819× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H1573 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 7.26 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0562× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 12.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.2× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0973× (z -11.0) |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0807× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-172 (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFNAR2]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[RIPK2]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[RTN4RL2]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[NFKBIZ]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[NFIL3]] | +0.53 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[GBP2]] | +0.52 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[SOD2]] | +0.51 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[PPP1R3B]] | +0.51 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[RNF19B]] | +0.50 | +0.48 / +0.51 | both halves | 2e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[MAP3K8]] | +0.50 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[NOD2]] | +0.50 | +0.51 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[ADM]] | +0.50 | +0.45 / +0.50 | both halves | 3e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRBC2]] | -0.48 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[PCNT]] | -0.46 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[ANKMY1]] | -0.46 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ZRANB3]] | -0.43 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[HCFC1]] | -0.41 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[GBX2-AS1]] | -0.41 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[PCBD2]] | -0.40 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[ELP4]] | -0.40 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[AGO2]] | -0.40 | -0.37 / -0.42 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL15]] | B | IL15 activity raises RNF144B's level | lines that do not express IL15 (10) vs lines expressing it (40) | 2.52× lower at baseline in the lines without IL15 | 0.005 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[DNAJC12]] | B | DNAJC12 activity raises RNF144B's level | lines that do not express DNAJC12 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without DNAJC12 | 0.037 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[TSPAN12]] | B | TSPAN12 activity raises RNF144B's level | lines that do not express TSPAN12 (13) vs lines expressing it (37) | 1.36× lower at baseline in the lines without TSPAN12 | 0.074 | ⚠ within organs, on part of the lines; also absent: ATP8A1, PPP1R9A, SH3BGRL2; maybe low, not absent |
| [[GBP2]] | B | GBP2 activity raises RNF144B's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without GBP2 | 0.092 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | RNF144B activity lowers TSPAN33's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 2.08× higher at baseline in the lines without RNF144B | 0.002 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[IL15]] | B | RNF144B activity raises IL15's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 2.41× lower at baseline in the lines without RNF144B | 0.005 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[ETS2]] | B | RNF144B activity raises ETS2's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without RNF144B | 0.007 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[MLLT3]] | B | RNF144B activity raises MLLT3's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 1.93× lower at baseline in the lines without RNF144B | 0.022 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[TRAF3IP2]] | B | RNF144B activity raises TRAF3IP2's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without RNF144B | 0.025 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[UGCG]] | B | RNF144B activity raises UGCG's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 1.71× lower at baseline in the lines without RNF144B | 0.035 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[NEDD9]] | B | RNF144B activity raises NEDD9's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 3.16× lower at baseline in the lines without RNF144B | 0.048 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[RNF19B]] | B | RNF144B activity raises RNF19B's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 1.44× lower at baseline in the lines without RNF144B | 0.059 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[SLC25A12]] | B | RNF144B activity lowers SLC25A12's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 1.29× higher at baseline in the lines without RNF144B | 0.061 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[SOD2]] | B | RNF144B activity raises SOD2's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 1.94× lower at baseline in the lines without RNF144B | 0.072 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| cells under [[Infigratinib (drug)]] 0.5 µM | B | RNF144B activity raises the cells' numbers under Infigratinib 0.5 µM (protects the cells) | lines that do not express RNF144B (15) vs lines expressing it (33) | the lines without RNF144B: 0.88× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[SQOR]] | B | RNF144B activity raises SQOR's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 2.13× lower at baseline in the lines without RNF144B | 0.086 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.439). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.3, 0.9); signed map (43.7, 12.1). **Vector** length 86.3, 21.1% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.7 | +18.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +7.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +7.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +4.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.8 | -6.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 144B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.3 — chr6:18,387,350-18,468,870 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA528A10.3, P53RFP; previously IBRDC2 |
| Gene groups (HGNC) | Ring finger proteins; RBR E3 ubiquitin ligases |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z419](https://www.uniprot.org/uniprotkb/Q7Z419) (E3 ubiquitin-protein ligase RNF144B):

> E3 ubiquitin-protein ligase which accepts ubiquitin from E2 ubiquitin-conjugating enzymes UBE2L3 and UBE2L6 in the form of a thioester and then directly transfers the ubiquitin to targeted substrates such as LCMT2, thereby promoting their degradation. Induces apoptosis via a p53/TP53-dependent but caspase-independent mechanism. Plays a crucial role in maintaining the genomic stability by controlling the degradation of multiple proteins involved in mitotic progression and DNA damage. Regulates …

**Summary**, from NCBI Gene [255488](https://www.ncbi.nlm.nih.gov/gene/255488):

> Enables ubiquitin-protein transferase activity. Involved in negative regulation of apoptotic process and ubiquitin-dependent protein catabolic process. Located in mitochondrial membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21578) · Entrez [255488](https://www.ncbi.nlm.nih.gov/gene/255488) · UniProt [Q7Z419](https://www.uniprot.org/uniprotkb/Q7Z419) · Ensembl [ENSG00000137393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137393)

## Data

Gene col 6007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6007); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6007]; `tensor/DDL_lfc|DDL_z.npy` [6007]; `embed/gene_vectors.npy` [6007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6007 or target_col == 6007). Every well: [[RNF144B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF144B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
