---
symbol: "LMNA"
type: "gene"
col: 8382
ensembl_id: "ENSG00000160789"
name: "lamin A/C"
location: "1q22"
module: 123
arm: "+"
pooled_cpm: 278.73
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# LMNA

*lamin A/C* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.70× (z +13.5, q 1e-38, up in 42 of 46 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.99× (z +6.6, q 3e-09, up in 43 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LGALS3]] (+0.67, fdr 7e-06), [[KLF2]] (+0.67, fdr 7e-06), [[ADGRE5]] (+0.62, fdr 1e-05); moves opposite to [[THOC5]] (-0.65, fdr 7e-06), [[ADPGK]] (-0.61, fdr 7e-06), [[METTL3]] (-0.59, fdr 1e-05).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ATP1B1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8382.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.70×** | +13.5 | 1e-38 | 42/46 (C32, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.05×** | +10.7 | 2e-24 | 46/47 (PANC-1, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.55×** | +8.6 | 1e-15 | 41/42 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.36×** | +7.9 | 3e-13 | 44/46 (NCI-H1573, SK-MEL-2, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.24×** | +7.8 | 9e-13 | 40/46 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.22×** | +7.1 | 1e-10 | 41/43 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.99×** | +6.6 | 3e-09 | 43/46 (C32, SW48, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.76×** | +5.4 | 4e-06 | 40/46 (C32, NCI-H460, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +4.6 | 2e-04 | 32/46 (HCT15, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.64×** | +4.6 | 3e-04 | 31/45 (C32, SW48, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.49×** | +3.8 | 0.007 | 30/46 (HCT15, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.45×** | +3.5 | 0.020 | 32/46 (NCI-H460, C32, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +3.2 | 0.056 | 27/46 (HCT15, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.088 | 33/45 (NCI-H23, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8382.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.509× | -3.4 | 0.24 | 35/47 (COLO 205, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~89% of this change | 0.707× | -3.2 | 0.24 | 26/46 (HT-29, A-172, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.733× | -3.0 | 0.24 | 28/46 (HS-578T, NCI-H1573, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.74 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8382. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 431 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +24.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.36× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 282 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +11.4) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.55× (z +9.8) | — |
| [[J82 (line)]] | alt | 243 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +13.8) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 132 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +19.2) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SW48 (line)]] | wt | 287 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.59× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 194 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +18.1) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.26× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 225 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +16.3) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H1573 (line)]] | alt | 129 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +19.5) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 264 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +17.1) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.92× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 176 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.25× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[PANC-1 (line)]] | alt | 274 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A498 (line)]] | wt | 362 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +14.2) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[AN3 CA (line)]] | alt | 171 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +13.3) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[COLO 205 (line)]] | alt | 163 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +14.3) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SNU-1 (line)]] | wt | 80.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.75× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 187 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.2) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[A549 (line)]] | wt | 310 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[HCT15 (line)]] | alt | 260 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.66× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 589 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HS-578T (line)]] | alt | 258 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +11.6) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[HT-29 (line)]] | alt | 452 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 270 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.6) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[KATO III (line)]] | alt | 327 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 323 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +10.9) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[Panc 03.27 (line)]] | alt | 213 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.58× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 85.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.89× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.51× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 353 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 900 (line)]] | alt | 438 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +11.8) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SW480 (line)]] | alt | 232 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[CFPAC-1 (line)]] | alt | 355 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +12.2) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[HOP62 (line)]] | alt | 328 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.3) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[LoVo (line)]] | wt | 213 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.1) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[LOX-IMVI (line)]] | wt | 186 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[NCI-H1792 (line)]] | alt | 165 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.6) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SHP-77 (line)]] | alt | 166 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 1088 (line)]] | alt | 377 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +8.5) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SW1417 (line)]] | alt | 240 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.6) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[A-172 (line)]] | wt | 761 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 58.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 354 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 289 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 172 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 323 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 393 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 194 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8382), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LGALS3]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS |
| [[KLF2]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ADGRE5]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CRIP2]] | +0.62 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[MIR23AHG]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[MARCKS]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[SERTAD2]] | +0.59 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[RHOB]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_APOPTOSIS |
| [[MAK]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[TUBB2A]] | +0.57 | +0.57 / +0.58 | both halves | 1e-05 | pathway: Mitotic Anaphase |
| [[JUND]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PLCD3]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC5]] | -0.65 | -0.74 / -0.61 | both halves | 7e-06 |  |
| [[ADPGK]] | -0.61 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[METTL3]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[IQCB1]] | -0.58 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[SNRNP40]] | -0.57 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[POP1]] | -0.56 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[MRPS15]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[RPUSD4]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.55 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ZFYVE9]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SLC30A6]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP1B1]] | B | ATP1B1 activity raises LMNA's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 2.49× lower at baseline in the lines without ATP1B1 | 8e-04 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[LGALS3]] | B | LGALS3 activity raises LMNA's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without LGALS3 | 0.011 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[SMAD7]] | B | SMAD7 activity raises LMNA's level | lines that do not express SMAD7 (5) vs lines expressing it (45) | 2.99× lower at baseline in the lines without SMAD7 | 0.029 | ⚠ within organs, on part of the lines; also absent: SFXN3, KIAA2012, PLSCR2; maybe low, not absent |
| [[RRAD]] | B | RRAD activity raises LMNA's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.38× lower at baseline in the lines without RRAD | 0.030 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[NFATC2]] | B | NFATC2 activity raises LMNA's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.60× lower at baseline in the lines without NFATC2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[GATA6]] | B | GATA6 activity weakens LMNA's drug response | lines that do not express GATA6 (16) vs lines expressing it (31) | the lines without GATA6 respond 1.20× as strongly (z diff -1.50); strongest at Homoharringtonine 0.5 µM: 2.81x vs 2.00x (z diff -3.0) | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3; target measured in part of the lines; artifact flags |
| [[KLF4]] | B | KLF4 activity raises LMNA's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 2.33× lower at baseline in the lines without KLF4 | 0.060 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |
| [[MARCKS]] | B | MARCKS activity raises LMNA's level | lines that do not express MARCKS (10) vs lines expressing it (40) | 1.90× lower at baseline in the lines without MARCKS | 0.085 | ⚠ within organs, on part of the lines; also absent: EPAS1, THBS1, PRICKLE2 |
| [[ZMIZ1]] | C | ZMIZ1 activity raises LMNA's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 2.06× lower at baseline in the lines without ZMIZ1 | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.665). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, 0.6); signed map (0.2, 23.0). **Vector** length 124, 52.5% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +7.2 | +13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.7 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.7 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.3 | +1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.4 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.3 | -2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~89% of this change | -7.3 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -2.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.9 | -2.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | +0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | lamin A/C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,082,572-156,140,081 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HGPS, MADA; previously LMN1, CMD1A, LGMD1B, PRO1, LMNL1 |
| Gene groups (HGNC) | Lamins |
| Hallmark sets | APOPTOSIS |
| Reactome | 30 pathways, smallest: Breakdown of the nuclear lamina; Depolymerization of the Nuclear Lamina; Initiation of Nuclear Envelope (NE) Reformation |
| Matched by | ensembl_id |

**Function**, from UniProt [P02545](https://www.uniprot.org/uniprotkb/P02545) (Prelamin-A/C):

> [Lamin-A/C]: Lamins are intermediate filament proteins that assemble into a filamentous meshwork, and which constitute the major components of the nuclear lamina, a fibrous layer on the nucleoplasmic side of the inner nuclear membrane. Lamins provide a framework for the nuclear envelope, bridging the nuclear envelope and chromatin, thereby playing an important role in nuclear assembly, chromatin organization, nuclear membrane and telomere dynamics. Lamin A and C also regulate matrix stiffness …

**Summary**, from NCBI Gene [4000](https://www.ncbi.nlm.nih.gov/gene/4000):

> The protein encoded by this gene is part of the nuclear lamina, a two-dimensional matrix of proteins located next to the inner nuclear membrane. The lamin family of proteins make up the matrix and are highly conserved in evolution. During mitosis, the lamina matrix is reversibly disassembled as the lamin proteins are phosphorylated. Lamin proteins are thought to be involved in nuclear stability, chromatin structure and gene expression. Vertebrate lamins consist of two types, A and B. …

**Accessions** — [HGNC:6636](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6636) · Entrez [4000](https://www.ncbi.nlm.nih.gov/gene/4000) · UniProt [P02545](https://www.uniprot.org/uniprotkb/P02545) · Ensembl [ENSG00000160789](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160789)

## Data

Gene col 8382: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8382); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8382, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8382]; `tensor/DDL_lfc|DDL_z.npy` [8382]; `embed/gene_vectors.npy` [8382]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8382 or target_col == 8382). Every well: [[LMNA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMNA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
