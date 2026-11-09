---
symbol: "NR1H2"
type: "gene"
col: 5205
ensembl_id: "ENSG00000131408"
name: "nuclear receptor subfamily 1 group H member 2"
location: "19q13.3"
module: 145
arm: "+"
pooled_cpm: 22.84
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# NR1H2

*nuclear receptor subfamily 1 group H member 2* — 19q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.47× (z +8.3, q 4e-14, up in 24 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.49× (z +4.5, q 0.001, up in 12 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.596× (z -11.2, q 3e-26, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OTUD5]] (+0.59, fdr 1e-05), [[INO80B]] (+0.59, fdr 3e-05), [[VPS4B]] (+0.58, fdr 1e-05); moves opposite to [[KLHL8]] (-0.50, fdr 3e-05), [[COX5A]] (-0.48, fdr 6e-05, ⚠ COX5A in the vector space only through flagged drug-doses), [[SMC6]] (-0.46, fdr 4e-05), [[WDR75]] (-0.46, fdr 4e-05).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5205.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.3 | 4e-14 | 24/44 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +5.6 | 6e-06 | 14/33 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +4.5 | 0.001 | 12/45 (LS 180, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.25×** | +4.5 | 0.001 | 18/40 (NCI-H2030, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.2 | 0.003 | 0/48 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.005 | 13/47 (HT-29, RKO, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.013 | 12/48 (RKO, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.031 | 5/46 (NCI-H460, HT-29, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.054 | 5/46 (A498, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.068 | 6/47 (C32, H4, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.16× | +3.1 | 0.086 | 2/48 (HT-29, SHP-77) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.10× | +3.0 | 0.12 | 11/48 (SNU-1, A-172, …) | all doses, flat | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5205.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.596×** | -11.2 | 3e-26 | 32/47 (J82, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.634×** | -9.7 | 1e-19 | 39/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.665×** | -8.8 | 2e-16 | 26/48 (HS-578T, SW 900, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.677×** | -8.4 | 5e-15 | 25/48 (HS-578T, J82, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.672×** | -8.2 | 2e-14 | 26/46 (RPMI-7951, A-427, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.702×** | -7.6 | 2e-12 | 26/47 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.709×** | -7.4 | 9e-12 | 28/48 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.788×** | -7.3 | 3e-11 | 25/47 (A-427, Panc 03.27, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.807×** | -6.6 | 4e-09 | 28/48 (RKO, SW 900, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.586×** | -6.0 | 9e-08 | 26/46 (Hs 766T, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.750×** | -6.0 | 1e-07 | 21/47 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.600×** | -5.8 | 4e-07 | 23/46 (HEC-1-A, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.766×** | -5.7 | 4e-07 | 23/48 (KATO III, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.768×** | -5.7 | 5e-07 | 19/47 (PANC-1, KATO III, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.768×** | -5.7 | 5e-07 | 19/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.639×** | -5.0 | 1e-05 | 15/44 (HEC-1-A, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.643×** | -5.0 | 2e-05 | 15/48 (HT-29, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.806×** | -4.7 | 9e-05 | 13/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.872× | -4.2 | 8e-04 | 10/48 (NCI-H2030, RPMI-7951, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.692×** | -4.1 | 8e-04 | 11/46 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.720×** | -4.0 | 0.001 | 6/48 (MIA PaCa-2, A498, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 25.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.27× (z +13.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 32.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -12.5) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 22.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.0) ⚠ cell-cycle shift, explains ~15% of this change |
| [[C-33 A (line)]] | alt | 46.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.282× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[HCT15 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -8.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +8.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 17.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.278× (z -9.7) |
| [[KATO III (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[LoVo (line)]] | wt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 23.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.326× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +11.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 19.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 32.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -11.1) |
| [[SW480 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.134× (z -10.1) ⚠ toxic |
| [[A-172 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OTUD5]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[INO80B]] | +0.59 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[VPS4B]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[DNAJB12]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ZNF646]] | +0.55 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[NUCB1]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PEX19]] | +0.53 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[WDR45]] | +0.53 | +0.26 / +0.58 | both halves | 4e-04 |  |
| [[SUPT7L]] | +0.53 | +0.32 / +0.61 | both halves | 2e-04 |  |
| [[RAB11B]] | +0.53 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[CYTH2]] | +0.53 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TINF2]] | +0.53 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL8]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[COX5A]] ⚠ | -0.48 | -0.43 / -0.39 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SMC6]] | -0.46 | -0.42 / -0.45 | both halves | 4e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[WDR75]] | -0.46 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[PALS2]] | -0.45 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[MTCH2]] | -0.45 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[SLC25A5]] | -0.45 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[PMS1]] | -0.45 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[ASB13]] | -0.44 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[MTX2]] | -0.44 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.193). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.5, -52.0); signed map (-3.2, -5.9). **Vector** length 76.3, 13.3% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +4.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.4 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +0.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -9.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.0 | -4.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -6.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 1 group H member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.3 — chr19:50,329,653-50,383,388 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NER, NER-I, RIP15, LXR-b, LXRb; previously UNR |
| Gene groups (HGNC) | Nuclear receptor subfamily 1 group H |
| Reactome | 18 pathways, smallest: NR1H2 & NR1H3 regulate gene expression linked to triglyceride lipolysis in adipose; NR1H2 & NR1H3 regulate gene expression to limit cholesterol uptake; NR1H2 & NR1H3 regulate gene expression to control bile acid homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P55055](https://www.uniprot.org/uniprotkb/P55055) (Oxysterols receptor LXR-beta):

> Nuclear receptor that exhibits a ligand-dependent transcriptional activation activity. Binds preferentially to double-stranded oligonucleotide direct repeats having the consensus half-site sequence 5'-AGGTCA-3' and 4-nt spacing (DR-4). Regulates cholesterol uptake through MYLIP-dependent ubiquitination of LDLR, VLDLR and LRP8; DLDLR and LRP8. Interplays functionally with RORA for the regulation of genes involved in liver metabolism (By similarity). Induces LPCAT3-dependent phospholipid …

**Summary**, from NCBI Gene [7376](https://www.ncbi.nlm.nih.gov/gene/7376):

> The liver X receptors, LXRA (NR1H3; MIM 602423) and LXRB, form a subfamily of the nuclear receptor superfamily and are key regulators of macrophage function, controlling transcriptional programs involved in lipid homeostasis and inflammation. The inducible LXRA is highly expressed in liver, adrenal gland, intestine, adipose tissue, macrophages, lung, and kidney, whereas LXRB is ubiquitously expressed. Ligand-activated LXRs form obligate heterodimers with retinoid X receptors (RXRs; see MIM …

**Accessions** — [HGNC:7965](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7965) · Entrez [7376](https://www.ncbi.nlm.nih.gov/gene/7376) · UniProt [P55055](https://www.uniprot.org/uniprotkb/P55055) · Ensembl [ENSG00000131408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131408)

## Data

Gene col 5205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5205); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5205]; `tensor/DDL_lfc|DDL_z.npy` [5205]; `embed/gene_vectors.npy` [5205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5205 or target_col == 5205). Every well: [[NR1H2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR1H2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
