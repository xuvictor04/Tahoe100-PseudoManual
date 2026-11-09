---
symbol: "BORA"
type: "gene"
col: 5816
ensembl_id: "ENSG00000136122"
name: "BORA aurora kinase A activator"
location: "13q21.33"
module: 22
arm: "+"
pooled_cpm: 25.1
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 29
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# BORA

*BORA aurora kinase A activator* — 13q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.05 µM: 1.42× (z +4.3, q 0.010, up in 20 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.34× (z +3.6, q 0.073, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 5.61×, Panc 03.27 4.25×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.405× (z -11.2, q 2e-26, down in 35 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.616× (z -6.0, q 2e-07, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTK]] (+0.83, fdr 7e-06), [[NUF2]] (+0.81, fdr 7e-06), [[PSRC1]] (+0.79, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5816.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 5.61×, Panc 03.27 4.25×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.42×** | +4.3 | 0.010 | 20/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +3.6 | 0.073 | 20/48 (Hs 766T, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.72×** | +3.5 | 0.073 | 12/46 (J82, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.32×** | +3.5 | 0.073 | 19/47 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +3.4 | 0.078 | 21/48 (KATO III, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.31×** | +3.3 | 0.093 | 18/48 (SW480, NCI-H23, …) | inconsistent across doses | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.22 | 13/48 (HOP62, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5816.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.405×** | -11.2 | 2e-26 | 35/42 (J82, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.518×** | -7.9 | 1e-12 | 23/33 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.548×** | -7.5 | 1e-11 | 30/47 (C32, J82, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -6.0 | 2e-07 | 28/47 (SW480, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.752×** | -5.0 | 6e-05 | 23/48 (A498, H4, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.679×** | -4.8 | 1e-04 | 23/47 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.691×** | -4.3 | 0.002 | 21/36 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.709×** | -4.1 | 0.002 | 21/48 (A498, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -4.1 | 0.002 | 23/48 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.715×** | -4.0 | 0.004 | 24/48 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.813×** | -3.7 | 0.013 | 19/48 (A498, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.815×** | -3.6 | 0.014 | 23/48 (H4, A498, …) | all doses, flat | low cells (technical?) |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.744×** | -3.4 | 0.028 | 13/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.763×** | -3.4 | 0.029 | 21/48 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.742×** | -3.4 | 0.029 | 11/48 (HOP62, SW480, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.749×** | -3.3 | 0.029 | 12/47 (HT-29, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.835× | -3.2 | 0.045 | 13/48 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.839× | -3.1 | 0.052 | 16/48 (AsPC-1, HT-29, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.781×** | -3.1 | 0.055 | 14/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.768×** | -3.0 | 0.057 | 14/46 (HOP62, SNU-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.784×** | -3.0 | 0.057 | 8/48 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.769×** | -3.0 | 0.067 | 11/48 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.790×** | -2.9 | 0.069 | 6/47 (RPMI-7951, SW480, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.638×** | -2.9 | 0.070 | 11/47 (A498, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 49.3 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0961× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.268× (z -13.9) |
| [[H4 (line)]] | wt | 27.9 | 0 | 4 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.211× (z -10.4) |
| [[J82 (line)]] | alt | 36.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -12.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 52.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.388× (z -9.1) |
| [[A-172 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.185× (z -10.1) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A-427 (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.129× (z -8.9) ⚠ toxic |
| [[A549 (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -10.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 9.60 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0898× (z -8.5) |
| [[LS 180 (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 23.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.212× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 9.79 | 0 | 1 | — | [[Elagolix sodium (drug)]] 5 µM 0.188× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -9.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +13.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0876× (z -11.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 22.6 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0780× (z -10.2) |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTK]] | +0.83 | +0.83 / +0.82 | both halves | 7e-06 | STRING 519 |
| [[NUF2]] | +0.81 | +0.81 / +0.81 | both halves | 7e-06 | STRING 432 |
| [[PSRC1]] | +0.79 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[CDCA3]] | +0.78 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[NEK2]] | +0.78 | +0.75 / +0.79 | both halves | 7e-06 | pathway: G2/M Transition; STRING 718 |
| [[PIF1]] | +0.77 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[CDCA8]] | +0.77 | +0.71 / +0.81 | both halves | 7e-06 | STRING 619 |
| [[TROAP]] | +0.76 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[PTTG1]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[KIF20A]] | +0.73 | +0.70 / +0.76 | both halves | 7e-06 | STRING 512 |
| [[KIF2C]] | +0.73 | +0.69 / +0.75 | both halves | 7e-06 | STRING 517 |
| [[GPSM2]] | +0.73 | +0.76 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.9, -56.5); signed map (-49.7, -40.4). **Vector** length 124, 35.1% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.56 to 60); *DREAM G2/M down* (control, mean cos +0.65 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.52 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.7 | +2.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +4.0 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | +2.9 | +3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.3 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.1 | +2.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -7.0 | -7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | -5.8 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -4.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | BORA aurora kinase A activator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q21.33 — chr13:72,727,749-72,756,198 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22624; previously C13orf34 |
| Reactome | 6 pathways, smallest: Cyclin A/B1/B2 associated events during G2/M transition; Regulation of PLK1 Activity at G2/M Transition; G2/M Transition |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PGQ7](https://www.uniprot.org/uniprotkb/Q6PGQ7) (Protein aurora borealis):

> Required for the activation of AURKA at the onset of mitosis.

**Summary**, from NCBI Gene [79866](https://www.ncbi.nlm.nih.gov/gene/79866):

> BORA is an activator of the protein kinase Aurora A (AURKA; MIM 603072), which is required for centrosome maturation, spindle assembly, and asymmetric protein localization during mitosis (Hutterer et al., 2006 [PubMed 16890155]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24724) · Entrez [79866](https://www.ncbi.nlm.nih.gov/gene/79866) · UniProt [Q6PGQ7](https://www.uniprot.org/uniprotkb/Q6PGQ7) · Ensembl [ENSG00000136122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136122)

## Data

Gene col 5816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5816); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5816]; `tensor/DDL_lfc|DDL_z.npy` [5816]; `embed/gene_vectors.npy` [5816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5816 or target_col == 5816). Every well: [[BORA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BORA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
