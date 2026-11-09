---
symbol: "USP30"
type: "gene"
col: 5651
ensembl_id: "ENSG00000135093"
name: "ubiquitin specific peptidase 30"
location: "12q24.11"
module: 183
arm: "+"
pooled_cpm: 15.55
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# USP30

*ubiquitin specific peptidase 30* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.79× (z +7.1, q 9e-10, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.467× (z -9.6, q 3e-19, down in 19 of 28 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.679× (z -7.2, q 1e-10, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYZL1]] (+0.75, fdr 7e-06), [[MED23]] (+0.71, fdr 7e-06), [[C12orf76]] (+0.71, fdr 7e-06); moves opposite to [[NEK10]] (-0.67, fdr 7e-06), [[SLFNL1-AS1]] (-0.66, fdr 1e-05), [[DDX5]] (-0.65, fdr 7e-06).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.79×** | +7.1 | 9e-10 | 33/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.32×** | +5.2 | 5e-05 | 23/48 (A498, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +4.7 | 5e-04 | 21/45 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.033 | 18/48 (AsPC-1, C32, …) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.092 | 13/45 (LS 180, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.092 | 12/48 (KATO III, AsPC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.60×** | +3.2 | 0.092 | 14/43 (HT-29, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.092 | 13/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 1.27× | +3.1 | 0.10 | 13/48 (RKO, A498, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.27× | +3.1 | 0.10 | 8/47 (LoVo, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5651.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.467×** | -9.6 | 3e-19 | 19/28 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.550×** | -7.9 | 1e-12 | 27/39 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.679×** | -7.2 | 1e-10 | 32/48 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.588×** | -7.0 | 5e-10 | 27/46 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.580×** | -6.9 | 7e-10 | 34/46 (C32, A-427, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.635×** | -5.7 | 9e-07 | 25/48 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.656×** | -5.3 | 8e-06 | 24/46 (A-172, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.767×** | -4.9 | 6e-05 | 20/47 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.698×** | -4.7 | 1e-04 | 23/48 (AN3 CA, C32, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.725×** | -4.2 | 0.001 | 21/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.642×** | -4.2 | 0.002 | 17/46 (Hs 766T, SNU-423, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.808×** | -4.0 | 0.004 | 17/48 (NCI-H661, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.727×** | -3.9 | 0.005 | 17/33 (HCT15, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.602×** | -3.5 | 0.020 | 18/46 (LS 180, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.775×** | -3.3 | 0.032 | 15/48 (SW48, KATO III, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.770×** | -3.3 | 0.034 | 13/47 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.798×** | -3.0 | 0.095 | 12/48 (NCI-H661, CFPAC-1, …) | inconsistent across doses |  |
| [[Rimonabant (drug)]] 5 µM |  | 0.854× | -2.9 | 0.099 | 11/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 16.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0477× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[C32 (line)]] | wt | 17.3 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0398× (z -16.5) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 26.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.0) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.471× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 24.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0885× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.161× (z -8.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -8.6) |
| [[HCT15 (line)]] | alt | 22.1 | 0 | 2 | — | [[Saquinavir (drug)]] 0.5 µM 0.106× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.304× (z -8.9) |
| [[SHP-77 (line)]] | alt | 22.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Palmatine (chloride) (drug)]] 0.5 µM 0.253× (z -8.8) |
| [[A-172 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0796× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.106× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0675× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.105× (z -8.5) |
| [[LoVo (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H1573 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0751× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[NCI-H1792 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0909× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SW480 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A498 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYZL1]] | +0.75 | +0.80 / +0.63 | both halves | 7e-06 |  |
| [[MED23]] | +0.71 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[C12orf76]] | +0.71 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[ZFP14]] | +0.71 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[PRUNE1]] | +0.71 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ZNF112]] | +0.69 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[MAPK3]] | +0.69 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[TERF1]] | +0.69 | +0.74 / +0.57 | both halves | 1e-05 |  |
| [[JKAMP]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[DYNC2LI1]] | +0.69 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[IFT52]] | +0.69 | +0.61 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK10]] | -0.67 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[SLFNL1-AS1]] | -0.66 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[DDX5]] | -0.65 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[DGKH]] | -0.65 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[PPIEL-1]] | -0.65 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[HNRNPAB]] | -0.64 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[MSRA]] | -0.64 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[EHBP1]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[AGO2]] | -0.62 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PKP4]] | -0.62 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[SATB2]] | -0.62 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.62 | -0.60 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises USP30's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABL1]] | B | ABL1 activity lowers USP30's level | compounds that target ABL1: 3 of 6 raise it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 2.0% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[BBS5]] | B | BBS5 activity raises USP30's level | lines that do not express BBS5 (6) vs lines expressing it (44) | 1.44× lower at baseline in the lines without BBS5 | 0.062 | ⚠ within organs, on part of the lines; also absent: GGT7, HLTF, FERMT2 |
| [[ZNF540]] | B | ZNF540 activity raises USP30's level | lines that do not express ZNF540 (5) vs lines expressing it (45) | 1.44× lower at baseline in the lines without ZNF540 | 0.072 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZFP14, ZNF573; maybe low, not absent |
| [[RRAGD]] | B | RRAGD activity raises USP30's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.25× lower at baseline in the lines without RRAGD | 0.076 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.880). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.3, -10.2); signed map (-30.7, -9.4). **Vector** length 93.2, 20.2% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.6 | +7.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +4.6 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +3.7 |
|  | [[NG25 (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +4.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +0.5 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -7.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -4.5 | -6.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.1 | -5.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.1 | -5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -7.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 30 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,023,089-109,088,023 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10702, FLJ40511 |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 6 pathways, smallest: Pexophagy; Selective autophagy; Macroautophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70CQ3](https://www.uniprot.org/uniprotkb/Q70CQ3) (Ubiquitin carboxyl-terminal hydrolase 30):

> Deubiquitinating enzyme tethered to the mitochondrial outer membrane that acts as a key inhibitor of mitophagy by counteracting the action of parkin (PRKN): hydrolyzes ubiquitin attached by parkin on target proteins, such as RHOT1/MIRO1 and TOMM20, thereby blocking parkin's ability to drive mitophagy. Preferentially cleaves 'Lys-6'- and 'Lys-11'-linked polyubiquitin chains, 2 types of linkage that participate in mitophagic signaling. Does not cleave efficiently polyubiquitin phosphorylated at …

**Summary**, from NCBI Gene [84749](https://www.ncbi.nlm.nih.gov/gene/84749):

> USP30, a member of the ubiquitin-specific protease family (see USP1, MIM 603478), is a novel mitochondrial deubiquitinating (DUB) enzyme (Nakamura and Hirose, 2008 [PubMed 18287522]).[supplied by OMIM, Dec 2008]

**Accessions** — [HGNC:20065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20065) · Entrez [84749](https://www.ncbi.nlm.nih.gov/gene/84749) · UniProt [Q70CQ3](https://www.uniprot.org/uniprotkb/Q70CQ3) · Ensembl [ENSG00000135093](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135093)

## Data

Gene col 5651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5651); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5651]; `tensor/DDL_lfc|DDL_z.npy` [5651]; `embed/gene_vectors.npy` [5651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5651 or target_col == 5651). Every well: [[USP30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
