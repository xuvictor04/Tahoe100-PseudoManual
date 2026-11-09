---
symbol: "MED9"
type: "gene"
col: 6481
ensembl_id: "ENSG00000141026"
name: "mediator complex subunit 9"
location: "17p11.2"
module: 36
arm: "+"
pooled_cpm: 17.1
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# MED9

*mediator complex subunit 9* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.53× (z +11.8, q 1e-29, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.623× (z -8.2, q 2e-13, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF322]] (+0.74, fdr 7e-06), [[GTF3C2]] (+0.72, fdr 7e-06), [[PSMF1]] (+0.71, fdr 7e-06); moves opposite to [[TEX14]] (-0.54, fdr 1e-05), [[YWHAZ]] (-0.53, fdr 3e-05), [[GLS]] (-0.51, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6481.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.53×** | +11.8 | 1e-29 | 40/48 (NCI-H460, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +8.1 | 2e-13 | 27/43 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +7.4 | 2e-11 | 26/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +7.1 | 1e-10 | 24/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +6.4 | 2e-08 | 24/47 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +5.9 | 4e-07 | 21/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +5.2 | 2e-05 | 16/46 (KATO III, HOP62, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.17× | +4.1 | 0.003 | 17/48 (AsPC-1, A498, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +3.9 | 0.006 | 11/47 (SW1417, Panc 03.27, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.019 | 9/47 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.21×** | +3.3 | 0.058 | 11/48 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.13× | +3.2 | 0.063 | 4/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6481.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.623×** | -8.2 | 2e-13 | 28/47 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.735×** | -7.8 | 2e-12 | 29/47 (C32, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.648×** | -7.5 | 1e-11 | 18/30 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -7.5 | 1e-11 | 29/47 (HepG2/C3A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -6.9 | 7e-10 | 27/48 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.695×** | -6.5 | 7e-09 | 19/40 (SHP-77, C-33 A, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -6.2 | 6e-08 | 24/48 (C32, SHP-77, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.768×** | -4.7 | 2e-04 | 20/48 (C32, A498, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.615×** | -4.6 | 3e-04 | 15/46 (CFPAC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.776×** | -4.5 | 3e-04 | 19/47 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -4.5 | 4e-04 | 3/48 (NCI-H1573, H4, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.801×** | -3.8 | 0.006 | 15/45 (C-33 A, SNU-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.814×** | -3.7 | 0.010 | 10/47 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.083 | 6/48 (LoVo, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 33.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -14.7) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -11.7) |
| [[A-172 (line)]] | wt | 13.8 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0759× (z -17.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.5) |
| [[A498 (line)]] | wt | 21.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.342× (z -9.6) |
| [[C-33 A (line)]] | alt | 26.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -10.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -9.6) |
| [[SHP-77 (line)]] | alt | 82.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -21.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0659× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 18.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -13.9) |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -9.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0620× (z -11.0) |
| [[J82 (line)]] | alt | 14.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0656× (z -20.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0721× (z -9.4) |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -10.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF322]] | +0.74 | +0.72 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[GTF3C2]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[PSMF1]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[ZNF551]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.66 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ZNF875]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[UBOX5]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[LINC03006-1]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[ZNF461]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[NDUFB7]] | +0.63 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ZNF169]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[MAFIP]] | +0.63 | +0.53 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX14]] | -0.54 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[GLS]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.505). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-30.8, -6.4); signed map (-16.4, -19.4). **Vector** length 87.7, 16.9% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.8 | +8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +11.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.7 | +7.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.7 | +1.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.2 | -7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -4.2 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -6.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -4.6 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.7 | -3.1 |
|  | [[Artemether (drug)]] 0.05 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,476,994-17,493,221 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10193, MED25 |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 8 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWA0](https://www.uniprot.org/uniprotkb/Q9NWA0) (Mediator of RNA polymerase II transcription subunit 9):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [55090](https://www.ncbi.nlm.nih.gov/gene/55090):

> The multiprotein Mediator complex is a coactivator required for activation of RNA polymerase II transcription by DNA bound transcription factors. The protein encoded by this gene is thought to be a subunit of the Mediator complex. This gene is located within the Smith-Magenis syndrome region on chromosome 17. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25487](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25487) · Entrez [55090](https://www.ncbi.nlm.nih.gov/gene/55090) · UniProt [Q9NWA0](https://www.uniprot.org/uniprotkb/Q9NWA0) · Ensembl [ENSG00000141026](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141026)

## Data

Gene col 6481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6481); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6481]; `tensor/DDL_lfc|DDL_z.npy` [6481]; `embed/gene_vectors.npy` [6481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6481 or target_col == 6481). Every well: [[MED9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
