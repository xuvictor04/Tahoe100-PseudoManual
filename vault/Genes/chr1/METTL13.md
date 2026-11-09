---
symbol: "METTL13"
type: "gene"
col: 199
ensembl_id: "ENSG00000010165"
name: "methyltransferase 13, eEF1A N-terminus and K55"
location: "1q24.3"
module: 107
arm: "+"
pooled_cpm: 16.46
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 8
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# METTL13

*methyltransferase 13, eEF1A N-terminus and K55* — 1q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.90× (z +18.7, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.646× (z -9.0, q 9e-17, down in 26 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.746× (z -6.1, q 2e-07, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF3C4]] (+0.72, fdr 7e-06), [[PALB2]] (+0.70, fdr 7e-06), [[SMG8]] (+0.68, fdr 7e-06); moves opposite to [[GRHL1]] (-0.59, fdr 9e-05), [[CHP1]] (-0.55, fdr 4e-05), [[SVIP]] (-0.54, fdr 2e-04).
> It is in [[Module 107]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +18.7 | 0e+00 | 42/46 (Panc 03.27, PANC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +8.8 | 3e-16 | 29/48 (NCI-H2347, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +7.7 | 3e-12 | 27/48 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.45×** | +7.7 | 3e-12 | 26/48 (NCI-H460, CFPAC-1, …) | two highest doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +7.1 | 2e-10 | 27/48 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +7.0 | 2e-10 | 22/46 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.38×** | +6.6 | 4e-09 | 23/48 (NCI-H460, CFPAC-1, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.37×** | +6.4 | 8e-09 | 21/47 (NCI-H460, CFPAC-1, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +6.0 | 2e-07 | 20/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +5.9 | 3e-07 | 17/46 (SW480, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +5.1 | 2e-05 | 15/43 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.59×** | +5.0 | 3e-05 | 11/44 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.5 | 3e-04 | 17/47 (PANC-1, LoVo, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +4.5 | 3e-04 | 14/47 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.24×** | +4.4 | 4e-04 | 10/47 (CFPAC-1, J82, …) | two highest doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.003 | 11/43 (NCI-H460, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.008 | 8/47 (NCI-H460, SW 900, …) | inconsistent across doses | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.008 | 6/45 (NCI-H1792, A498, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.5 | 0.011 | 17/45 (Panc 03.27, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.2 | 0.029 | 15/47 (NCI-H460, A-172, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.038 | 9/45 (NCI-H1573, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 199.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.646×** | -9.0 | 9e-17 | 26/40 (SNU-423, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.650×** | -8.9 | 2e-16 | 28/46 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.692×** | -7.1 | 3e-10 | 18/34 (NCI-H1573, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.746×** | -6.1 | 2e-07 | 21/48 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.816×** | -4.1 | 0.006 | 13/30 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Rifaximin (drug)]] 5 µM |  | **0.821×** | -3.9 | 0.008 | 7/46 (AsPC-1, NCI-H2030, …) | top dose only | position effect removed |
| [[Cyclosporin A (drug)]] 5 µM |  | **0.829×** | -3.9 | 0.008 | 7/47 (NCI-H2030, LOX-IMVI, …) | top dose only | position effect removed |
| [[Cytarabine (drug)]] 5 µM |  | **0.824×** | -3.9 | 0.008 | 10/47 (RPMI-7951, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.889× | -3.4 | 0.036 | 12/48 (A-172, MIA PaCa-2, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.860× | -3.1 | 0.10 | 13/47 (CFPAC-1, SHP-77, …) | all doses, flat |  |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | 0.865× | -3.0 | 0.13 | 9/47 (SW48, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 13.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0859× (z -14.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -11.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 19.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -18.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +11.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -9.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 10.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -9.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0852× (z -11.0) |
| [[HOP62 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0864× (z -9.6) |
| [[LS 180 (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 16.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +11.7) | — |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -12.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0498× (z -16.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -13.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 13.1 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.105× (z -8.6) |
| [[A549 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C4]] | +0.72 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[PALB2]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[SMG8]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ZNF7]] | +0.67 | +0.57 / +0.64 | both halves | 8e-06 |  |
| [[MIEF1]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[GEMIN4]] | +0.64 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[NOP16]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[DUS2]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SCO1]] | +0.62 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[TBRG4]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TRMT12]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRHL1]] | -0.59 | -0.36 / -0.60 | both halves | 9e-05 |  |
| [[CHP1]] | -0.55 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[SVIP]] | -0.54 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[EMC10]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[PRKCI]] | -0.52 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[NKTR]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.609). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-47.0, 6.9); signed map (-4.9, -29.2). **Vector** length 77.9, 13.5% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +18.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.7 | +8.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | -7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.6 | -8.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 13, eEF1A N-terminus and K55 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.3 — chr1:171,781,660-171,814,023 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-01, FEAT; previously KIAA0859, DFNM1, EEF1AKNMT |
| Gene groups (HGNC) | 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases; N- and C-terminal methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6R0](https://www.uniprot.org/uniprotkb/Q8N6R0) (eEF1A lysine and N-terminal methyltransferase):

> Dual methyltransferase that catalyzes methylation of elongation factor 1-alpha (EEF1A1 and EEF1A2) at two different positions, and is therefore involved in the regulation of mRNA translation. Via its C-terminus, methylates EEF1A1 and EEF1A2 at the N-terminal residue 'Gly-2'. Via its N-terminus dimethylates EEF1A1 and EEF1A2 at residue 'Lys-55'. Has no activity towards core histones H2A, H2B, H3 and H4.

**Summary**, from NCBI Gene [51603](https://www.ncbi.nlm.nih.gov/gene/51603):

> Enables protein-lysine N-methyltransferase activity. Predicted to be involved in methylation. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24248](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24248) · Entrez [51603](https://www.ncbi.nlm.nih.gov/gene/51603) · UniProt [Q8N6R0](https://www.uniprot.org/uniprotkb/Q8N6R0) · Ensembl [ENSG00000010165](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010165)

## Data

Gene col 199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 199); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 199]; `tensor/DDL_lfc|DDL_z.npy` [199]; `embed/gene_vectors.npy` [199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 199 or target_col == 199). Every well: [[METTL13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
