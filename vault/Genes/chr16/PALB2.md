---
symbol: "PALB2"
type: "gene"
col: 1360
ensembl_id: "ENSG00000083093"
name: "partner and localizer of BRCA2"
location: "16p12.2"
module: 1
arm: "+"
pooled_cpm: 16.45
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PALB2

*partner and localizer of BRCA2* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.41× (z +8.0, q 6e-13, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.540× (z -10.2, q 1e-21, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UMPS]] (+0.73, fdr 7e-06), [[METTL13]] (+0.70, fdr 7e-06), [[QTRT2]] (+0.68, fdr 7e-06); moves opposite to [[CHP1]] (-0.60, fdr 4e-05), [[GRHL1]] (-0.60, fdr 1e-04), [[SHF]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +8.0 | 6e-13 | 24/48 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.35×** | +7.0 | 5e-10 | 27/46 (PANC-1, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.54×** | +6.8 | 1e-09 | 25/41 (SW480, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.0 | 2e-07 | 24/46 (NCI-H460, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +5.4 | 8e-06 | 21/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.35×** | +4.9 | 8e-05 | 18/47 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.33×** | +4.7 | 2e-04 | 16/47 (J82, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 0.001 | 11/47 (Hs 766T, LS 180, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.29×** | +4.1 | 0.003 | 14/46 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.004 | 6/45 (SK-MEL-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.004 | 17/48 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.8 | 0.008 | 12/48 (A-427, Hs 766T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.24×** | +3.4 | 0.029 | 9/47 (PANC-1, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.031 | 5/46 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.055 | 9/47 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.078 | 8/47 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.083 | 3/46 (PANC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1360.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.540×** | -10.2 | 1e-21 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.566×** | -9.4 | 1e-18 | 28/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.760×** | -6.4 | 3e-08 | 22/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -6.2 | 8e-08 | 25/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -6.2 | 8e-08 | 16/28 (SNU-423, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.744×** | -4.9 | 9e-05 | 19/47 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.764×** | -4.5 | 7e-04 | 18/40 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.824×** | -3.2 | 0.099 | 13/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.832× | -3.0 | 0.15 | 11/47 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.7 | 1 (1 ⚠) | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.9) ⚠ cell-cycle shift, explains ~24% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -14.2) |
| [[KATO III (line)]] | alt | 30.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -15.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 22.6 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.271× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -12.7) |
| [[A-172 (line)]] | wt | 18.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -10.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 18.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -10.1) |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 20.3 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0787× (z -16.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A498 (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.342× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 1 | — | [[PF-06260933 (drug)]] 5 µM 0.0543× (z -9.9) |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -9.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 8.18 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.149× (z -8.9) |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.164× (z -10.0) ⚠ transcription drop |
| [[hTERT-HPNE (line)]] | wt | 9.91 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.118× (z -8.8) |
| [[J82 (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -13.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0739× (z -11.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0564× (z -17.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0963× (z -16.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UMPS]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[METTL13]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[QTRT2]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[TRMT5]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[PPP1R8]] | +0.67 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[NOL11]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[GTF3C4]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[TRMT61B]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[DDX20]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[C1orf109]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[NUDT19]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SCO1]] | +0.62 | +0.64 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHP1]] | -0.60 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[GRHL1]] | -0.60 | -0.34 / -0.65 | both halves | 1e-04 |  |
| [[SHF]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[NPTN]] | -0.53 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[GTF2IP4]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[OAZ1]] | -0.52 | -0.34 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.581). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-46.9, 6.9); signed map (-4.9, -29.3). **Vector** length 82.1, 15.1% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial mRNA modification* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | +5.2 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.2 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +0.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.6 | -6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.5 | -4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -9.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | partner and localizer of BRCA2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:23,603,160-23,641,321 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21816, FANCN |
| Gene groups (HGNC) | WD repeat domain containing; FA complementation groups |
| Reactome | 22 pathways, smallest: Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA2/RAD51/RAD51C binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YC2](https://www.uniprot.org/uniprotkb/Q86YC2) (Partner and localizer of BRCA2):

> Plays a critical role in homologous recombination repair (HRR) through its ability to recruit BRCA2 and RAD51 to DNA breaks. Strongly stimulates the DNA strand-invasion activity of RAD51, stabilizes the nucleoprotein filament against a disruptive BRC3-BRC4 polypeptide and helps RAD51 to overcome the suppressive effect of replication protein A (RPA). Functionally cooperates with RAD51AP1 in promoting of D-loop formation by RAD51. Serves as the molecular scaffold in the formation of the …

**Summary**, from NCBI Gene [79728](https://www.ncbi.nlm.nih.gov/gene/79728):

> This gene encodes a protein that may function in tumor suppression. This protein binds to and colocalizes with the breast cancer 2 early onset protein (BRCA2) in nuclear foci and likely permits the stable intranuclear localization and accumulation of BRCA2. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:26144](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26144) · Entrez [79728](https://www.ncbi.nlm.nih.gov/gene/79728) · UniProt [Q86YC2](https://www.uniprot.org/uniprotkb/Q86YC2) · Ensembl [ENSG00000083093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083093)

## Data

Gene col 1360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1360); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1360]; `tensor/DDL_lfc|DDL_z.npy` [1360]; `embed/gene_vectors.npy` [1360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1360 or target_col == 1360). Every well: [[PALB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PALB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
