---
symbol: "HECTD1"
type: "gene"
col: 1692
ensembl_id: "ENSG00000092148"
name: "HECT domain E3 ubiquitin protein ligase 1"
location: "14q12"
module: 99
arm: "+"
pooled_cpm: 180.99
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# HECTD1

*HECT domain E3 ubiquitin protein ligase 1* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.22× (z +5.3, q 7e-05, up in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~17% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.22× (z +5.1, q 9e-05, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 2.31×, SK-MEL-2 2.12×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Budesonide (drug)]] 0.5 µM in 2 lines (SNU-423 2.02×, NCI-H460 1.63×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 2.82×; ⚠ cell-cycle shift, explains ~17% of this change); [[Dexamethasone (drug)]] 0.5 µM in 1 line (NCI-H460 1.71×); [[Digitoxin (drug)]] 0.5 µM in 1 line (CFPAC-1 2.01×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.355× (z -26.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYND11]] (+0.68, fdr 7e-06), [[STXBP5]] (+0.67, fdr 7e-06), [[DNAJC11]] (+0.62, fdr 1e-05); moves opposite to [[RAB8B]] (-0.62, fdr 8e-06), [[UBA6]] (-0.62, fdr 1e-05), [[ANKRD37]] (-0.62, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1692.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 2.31×, SK-MEL-2 2.12×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Budesonide (drug)]] 0.5 µM in 2 lines (SNU-423 2.02×, NCI-H460 1.63×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (COLO 205 2.82×; ⚠ cell-cycle shift, explains ~17% of this change); [[Dexamethasone (drug)]] 0.5 µM in 1 line (NCI-H460 1.71×); [[Digitoxin (drug)]] 0.5 µM in 1 line (CFPAC-1 2.01×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.22×** | +5.3 | 7e-05 | 25/48 (COLO 205, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +5.1 | 9e-05 | 24/48 (CFPAC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.5 | 0.002 | 22/48 (CFPAC-1, HCT15, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.19× | +4.3 | 0.002 | 22/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.1 | 0.005 | 18/48 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.6 | 0.031 | 19/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.15× | +3.5 | 0.037 | 17/48 (NCI-H23, RPMI-7951, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | 1.13× | +3.3 | 0.079 | 15/48 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.087 | 21/48 (MIA PaCa-2, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.12× | +3.0 | 0.14 | 14/48 (NCI-H460, SNU-423, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.355×** | -26.9 | 0e+00 | 48/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.377×** | -25.4 | 0e+00 | 48/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.451×** | -20.7 | 0e+00 | 47/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.672×** | -10.3 | 9e-23 | 43/48 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.777×** | -9.3 | 2e-18 | 31/49 (A498, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.782×** | -9.0 | 2e-17 | 34/48 (NCI-H2347, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.745×** | -7.6 | 2e-12 | 36/49 (HT-29, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.763×** | -6.5 | 6e-09 | 31/45 (SW48, SHP-77, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.786×** | -6.2 | 3e-08 | 33/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.797×** | -5.6 | 1e-06 | 30/47 (A498, HT-29, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.685×** | -5.1 | 2e-05 | 35/49 (SW480, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.849× | -4.2 | 0.001 | 19/48 (J82, A-427, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 0.842× | -4.2 | 0.001 | 23/50 (A498, A-427, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.851× | -3.9 | 0.003 | 16/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.898× | -3.9 | 0.003 | 10/48 (BT-474, KATO III, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.921× | -3.0 | 0.085 | 3/48 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.891× | -3.0 | 0.085 | 10/48 (BT-474, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 292 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -26.2) |
| [[HT-29 (line)]] | alt | 244 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -21.5) |
| [[NCI-H460 (line)]] | wt | 185 | 4 | 4 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 1.71× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.320× (z -21.0) |
| [[CFPAC-1 (line)]] | alt | 248 | 3 (2 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.01× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.363× (z -14.1) |
| [[LoVo (line)]] | wt | 267 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 2.79× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.217× (z -26.4) |
| [[A498 (line)]] | wt | 167 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -20.1) |
| [[KATO III (line)]] | alt | 240 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -23.2) |
| [[A-427 (line)]] | wt | 176 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -19.7) |
| [[A549 (line)]] | wt | 229 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -15.2) |
| [[COLO 205 (line)]] | alt | 209 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.82× (z +12.0) ⚠ cell-cycle shift, explains ~17% of this change | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -16.9) |
| [[J82 (line)]] | alt | 125 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.386× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 295 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -17.5) |
| [[NCI-H2347 (line)]] | alt | 228 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.263× (z -21.4) |
| [[PANC-1 (line)]] | alt | 147 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -20.1) |
| [[SW48 (line)]] | wt | 266 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -13.9) |
| [[AN3 CA (line)]] | alt | 202 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.312× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 133 | 1 | 3 | [[TAK-901 (drug)]] 0.05 µM 1.73× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.344× (z -17.6) |
| [[NCI-H1792 (line)]] | alt | 228 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -18.8) |
| [[NCI-H23 (line)]] | alt | 192 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.31× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.444× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 203 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -20.0) |
| [[SHP-77 (line)]] | alt | 195 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.364× (z -15.4) |
| [[SNU-1 (line)]] | wt | 196 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.349× (z -12.6) |
| [[SNU-423 (line)]] | alt | 166 | 1 | 3 | [[Budesonide (drug)]] 0.5 µM 2.02× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.321× (z -14.8) |
| [[SW 900 (line)]] | alt | 164 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -15.4) |
| [[SW1417 (line)]] | alt | 148 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.373× (z -14.2) |
| [[SW480 (line)]] | alt | 157 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -25.3) |
| [[A-172 (line)]] | wt | 102 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.440× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 138 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -16.8) |
| [[BT-474 (line)]] | alt | 260 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -15.8) |
| [[C-33 A (line)]] | alt | 199 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.384× (z -13.0) |
| [[C32 (line)]] | wt | 119 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.399× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 164 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.398× (z -11.9) |
| [[HOP62 (line)]] | alt | 123 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.423× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 128 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.430× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 169 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -19.3) |
| [[NCI-H2030 (line)]] | alt | 244 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.439× (z -13.1) |
| [[RKO (line)]] | wt | 162 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -15.7) |
| [[SK-MEL-2 (line)]] | alt | 125 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.432× (z -12.2) |
| [[CHP-212 (line)]] | wt | 146 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.299× (z -9.9) |
| [[HCT15 (line)]] | alt | 204 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.490× (z -9.7) |
| [[Hs 766T (line)]] | wt | 99.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -12.0) |
| [[HS-578T (line)]] | alt | 88.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.438× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 136 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.434× (z -9.1) |
| [[H4 (line)]] | wt | 138 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.362× (z -10.8) |
| [[NCI-H2122 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 365 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 169 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[STXBP5]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.62 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CUL1]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[DNAJB12]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[DNAJB14]] | +0.61 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ZFX]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[MED1]] | +0.60 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[CDC42BPA]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CPSF2]] | +0.58 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[TRAPPC8]] | +0.58 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[C11orf58]] | +0.57 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB8B]] | -0.62 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[UBA6]] | -0.62 | -0.54 / -0.52 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[ANKRD37]] | -0.62 | -0.62 / -0.51 | both halves | 1e-05 | same gene group |
| [[ICAM5]] | -0.60 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[TNFRSF11A]] | -0.60 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[GPR160]] | -0.58 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[AHDC1]] | -0.58 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[CNGA1]] | -0.56 | -0.37 / -0.61 | both halves | 7e-05 |  |
| [[AZIN2]] | -0.55 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[FSCN1]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[LPCAT2]] | -0.54 | -0.48 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises HECTD1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises HECTD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GCLC]] | C | GCLC activity raises HECTD1's level | lines that do not express GCLC (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without GCLC | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LRRC8B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction -0.447). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.9, 35.8); signed map (18.4, -28.7). **Vector** length 123, 38.1% of its response variance represented; |z| ≥ 3 in 1,556 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +6.2 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.3 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | +5.1 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +4.8 | +5.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.8 | +3.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | +4.7 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.0 | -7.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.6 | -10.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.0 | -20.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.0 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | HECT domain E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:31,100,117-31,207,804 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1131 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Armadillo like helical domain containing; HECT domain E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULT8](https://www.uniprot.org/uniprotkb/Q9ULT8) (E3 ubiquitin-protein ligase HECTD1):

> E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Mediates 'Lys-63'-linked polyubiquitination of HSP90AA1 which leads to its intracellular localization and reduced secretion (By similarity). Negatively regulating HSP90AA1 secretion in cranial mesenchyme cells may impair their emigration and may be essential for the correct development of the cranial neural folds …

**Summary**, from NCBI Gene [25831](https://www.ncbi.nlm.nih.gov/gene/25831):

> Enables ubiquitin protein ligase activity. Predicted to be involved in positive regulation of proteasomal ubiquitin-dependent protein catabolic process. Predicted to act upstream of or within several processes, including chordate embryonic development; circulatory system development; and protein ubiquitination. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20157) · Entrez [25831](https://www.ncbi.nlm.nih.gov/gene/25831) · UniProt [Q9ULT8](https://www.uniprot.org/uniprotkb/Q9ULT8) · Ensembl [ENSG00000092148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092148)

## Data

Gene col 1692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1692); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1692]; `tensor/DDL_lfc|DDL_z.npy` [1692]; `embed/gene_vectors.npy` [1692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1692 or target_col == 1692). Every well: [[HECTD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HECTD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
