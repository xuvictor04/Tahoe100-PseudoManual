---
symbol: "C4orf3"
type: "gene"
col: 8866
ensembl_id: "ENSG00000164096"
name: "allregulin"
location: "4q26"
module: 79
arm: "+"
pooled_cpm: 66.61
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# C4orf3

*allregulin* — 4q26

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 3.28×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.240× (z -18.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM162A]] (+0.71, fdr 7e-06), [[FUT11]] (+0.69, fdr 7e-06), [[HILPDA]] (+0.69, fdr 7e-06); moves opposite to [[CCT6P1]] (-0.62, fdr 1e-05), [[U2SURP]] (-0.60, fdr 1e-05), [[SGPL1]] (-0.58, fdr 7e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8866.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 3.28×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Arbutin (drug)]] 5 µM |  | 1.45× | +3.3 | 0.25 | 35/48 (SNU-423, H4, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.43× | +3.3 | 0.25 | 38/48 (NCI-H1792, Panc 03.27, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~83% of this change | 1.39× | +3.1 | 0.41 | 28/48 (A-172, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8866.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.240×** | -18.6 | 0e+00 | 48/48 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.366×** | -9.3 | 6e-18 | 46/48 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.386×** | -8.4 | 7e-15 | 45/47 (HT-29, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.420×** | -7.7 | 2e-12 | 44/48 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.473×** | -6.9 | 7e-10 | 45/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.528×** | -5.9 | 4e-07 | 44/48 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.300×** | -5.5 | 3e-06 | 46/49 (LoVo, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.572×** | -5.1 | 2e-05 | 44/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.508×** | -5.0 | 4e-05 | 41/48 (C32, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.378×** | -4.5 | 5e-04 | 33/45 (HS-578T, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -4.4 | 7e-04 | 34/49 (J82, HT-29, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.390×** | -4.3 | 8e-04 | 35/49 (HT-29, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -4.1 | 0.002 | 34/48 (AN3 CA, H4, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.416×** | -4.0 | 0.002 | 36/48 (Panc 03.27, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.664×** | -3.8 | 0.007 | 40/48 (NCI-H2030, KATO III, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.669×** | -3.7 | 0.008 | 29/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.681×** | -3.5 | 0.014 | 38/48 (HOP62, NCI-H1573, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.691×** | -3.4 | 0.022 | 33/48 (HT-29, SNU-1, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.703×** | -3.2 | 0.036 | 28/48 (AsPC-1, NCI-H661, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.718×** | -3.0 | 0.068 | 27/48 (NCI-H23, HT-29, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 99.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -17.5) |
| [[LoVo (line)]] | wt | 89.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0692× (z -25.9) |
| [[HT-29 (line)]] | alt | 75.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.9) |
| [[NCI-H1573 (line)]] | alt | 129 | 1 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 3.28× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -21.0) |
| [[AN3 CA (line)]] | alt | 69.2 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0850× (z -11.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -10.2) |
| [[LS 180 (line)]] | wt | 139 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -18.4) |
| [[NCI-H460 (line)]] | wt | 47.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -20.1) |
| [[BT-474 (line)]] | alt | 81.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -16.7) |
| [[C-33 A (line)]] | alt | 116 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -15.6) |
| [[C32 (line)]] | wt | 78.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -14.2) |
| [[HCT15 (line)]] | alt | 119 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -16.6) |
| [[HEC-1-A (line)]] | alt | 66.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -14.3) |
| [[HOP62 (line)]] | alt | 65.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 80.1 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.163× (z -13.3) |
| [[NCI-H2347 (line)]] | alt | 82.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.6) |
| [[Panc 03.27 (line)]] | alt | 54.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 122 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -18.9) |
| [[SK-MEL-2 (line)]] | alt | 55.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0722× (z -23.3) |
| [[SW 900 (line)]] | alt | 70.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -19.6) |
| [[SW480 (line)]] | alt | 35.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -12.4) |
| [[A549 (line)]] | wt | 43.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 61.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 89.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -15.4) |
| [[COLO 205 (line)]] | alt | 81.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -16.9) |
| [[H4 (line)]] | wt | 95.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -12.9) |
| [[HepG2_C3A (line)]] | wt | 89.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.6) |
| [[HS-578T (line)]] | alt | 61.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.1) |
| [[J82 (line)]] | alt | 60.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -16.1) |
| [[LOX-IMVI (line)]] | wt | 47.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -13.3) |
| [[NCI-H1792 (line)]] | alt | 69.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -20.0) |
| [[NCI-H2030 (line)]] | alt | 70.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -19.3) |
| [[PANC-1 (line)]] | alt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -13.5) |
| [[RKO (line)]] | wt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -13.7) |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.5) |
| [[SNU-1 (line)]] | wt | 73.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -15.4) |
| [[SNU-423 (line)]] | alt | 58.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -16.5) |
| [[SW1417 (line)]] | alt | 51.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -11.4) |
| [[SW48 (line)]] | wt | 66.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -9.4) |
| [[A-172 (line)]] | wt | 58.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 69.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM162A]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 | STRING 450 |
| [[FUT11]] | +0.69 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.69 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[P4HA1]] | +0.68 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[MIF]] | +0.68 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[TXNDC17]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[BNIP3]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ALDOC]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SEC61G]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[ALDOA]] | +0.62 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[PCSK1N]] | +0.62 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[SLC25A4]] | +0.62 | +0.40 / +0.54 | both halves | 5e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT6P1]] | -0.62 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[U2SURP]] | -0.60 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[SGPL1]] | -0.58 | -0.38 / -0.63 | both halves | 7e-05 |  |
| [[ADSS2]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | -0.56 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SBDSP1]] | -0.55 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[EWSR1]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SF1]] | -0.53 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[IMPACT]] | -0.52 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[MCCC2]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[CCT6P3]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[SLC25A24]] | -0.52 | -0.37 / -0.50 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.5, -16.9); signed map (-37.4, 18.5). **Vector** length 113, 42.1% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.4 | +2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.4 | +2.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +6.4 | +2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.4 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.0 | +3.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.1 | -8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.0 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.6 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.4 | +1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.0 | -5.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -3.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | allregulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q26 — chr4:119,296,419-119,304,445 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCVFTP1, ALN; previously C4orf3 |
| Gene groups (HGNC) | Regulins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVX3](https://www.uniprot.org/uniprotkb/Q8WVX3) (Sarcoplasmic/endoplasmic reticulum calcium ATPase regulator ARLN):

> Inhibits the activity of the calcium ATPases ATP2A2/SERCA2 and ATP2A3/SERCA3 by decreasing their apparent affinity for Ca(2+).

**Summary**, from NCBI Gene [401152](https://www.ncbi.nlm.nih.gov/gene/401152):

> Predicted to act upstream of or within negative regulation of ATPase-coupled calcium transmembrane transporter activity. Predicted to be located in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19225](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19225) · Entrez [401152](https://www.ncbi.nlm.nih.gov/gene/401152) · UniProt [Q8WVX3](https://www.uniprot.org/uniprotkb/Q8WVX3) · Ensembl [ENSG00000164096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164096)

## Data

Gene col 8866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8866); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8866]; `tensor/DDL_lfc|DDL_z.npy` [8866]; `embed/gene_vectors.npy` [8866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8866 or target_col == 8866). Every well: [[C4orf3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C4orf3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
