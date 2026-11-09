---
symbol: "SLC19A1"
type: "gene"
col: 10412
ensembl_id: "ENSG00000173638"
name: "solute carrier family 19 member 1"
location: "21q22.3"
module: 4
arm: "+"
pooled_cpm: 8.85
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# SLC19A1

*solute carrier family 19 member 1* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.89× (z +9.2, q 1e-17, up in 34 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.76× (z +8.2, q 3e-14, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.513× (z -13.8, q 1e-40, down in 33 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM201]] (+0.71, fdr 7e-06), [[MAT2A]] (+0.70, fdr 7e-06), [[POLR3H]] (+0.68, fdr 7e-06); moves opposite to [[ZMYM5]] (-0.63, fdr 7e-06), [[SYNRG]] (-0.61, fdr 1e-05), [[PPP1R12A]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[IGSF9B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10412.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.89×** | +9.2 | 1e-17 | 34/47 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +9.0 | 9e-17 | 16/23 (LoVo, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +8.2 | 3e-14 | 26/45 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +6.2 | 1e-07 | 14/30 (HS-578T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.7 | 2e-06 | 9/14 (SW1417, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 4e-04 | 14/43 (NCI-H460, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.027 | 10/45 (HEC-1-A, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.032 | 12/45 (NCI-H1792, LS 180, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.27×** | +3.5 | 0.032 | 12/47 (SW1417, CFPAC-1, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.064 | 4/43 (SW1417, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.23× | +3.0 | 0.13 | 11/38 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10412.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.513×** | -13.8 | 1e-40 | 33/44 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.524×** | -9.1 | 3e-17 | 31/45 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -8.5 | 3e-15 | 22/44 (NCI-H23, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.563×** | -8.4 | 6e-15 | 25/43 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.610×** | -7.0 | 4e-10 | 26/44 (NCI-H23, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -5.2 | 2e-05 | 18/44 (LS 180, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.705×** | -5.1 | 2e-05 | 17/47 (RKO, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.538×** | -4.7 | 2e-04 | 11/46 (MIA PaCa-2, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.750×** | -4.2 | 0.002 | 12/47 (LS 180, SW1417, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.754×** | -4.2 | 0.002 | 17/46 (SNU-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.757×** | -4.1 | 0.002 | 13/46 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.827×** | -3.5 | 0.022 | 7/46 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.796×** | -3.3 | 0.035 | 9/46 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -3.3 | 0.039 | 17/48 (LS 180, A498, …) | top dose only | low cells (technical?) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.855× | -3.3 | 0.043 | 6/45 (HOP62, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.814×** | -3.0 | 0.089 | 11/45 (Hs 766T, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10412. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 19.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -14.0) |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -11.9) |
| [[A-427 (line)]] | wt | 16.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -11.7) |
| [[C32 (line)]] | wt | 4.55 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.0460× (z -10.1) |
| [[COLO 205 (line)]] | alt | 6.72 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +12.3) | [[Clobetasol propionate (drug)]] 0.5 µM 0.0918× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -13.8) |
| [[SW480 (line)]] | alt | 9.67 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -12.9) |
| [[A498 (line)]] | wt | 9.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.8) |
| [[A549 (line)]] | wt | 6.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.3) |
| [[BT-474 (line)]] | alt | 6.38 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.0564× (z -10.5) |
| [[H4 (line)]] | wt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -8.8) |
| [[Hs 766T (line)]] | wt | 5.33 | 0 | 1 | — | [[Torkinib (drug)]] 0.05 µM 0.0704× (z -9.6) |
| [[HT-29 (line)]] | alt | 4.94 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -8.9) |
| [[J82 (line)]] | alt | 7.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -14.9) |
| [[NCI-H1573 (line)]] | alt | 5.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 6.44 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.0) |
| [[RKO (line)]] | wt | 13.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0521× (z -13.3) |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0789× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.09 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.106× (z -8.8) |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0773× (z -9.1) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SW48 (line)]] | wt | 20.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.207× (z -9.8) |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10412), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM201]] | +0.71 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MAT2A]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[POLR3H]] | +0.68 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[BOP1]] | +0.67 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[NOC2L]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PGAM5]] | +0.67 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[MAPKAPK3]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[SORD]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[MYBBP1A]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[KAT2A]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.64 | +0.53 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | -0.63 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[SYNRG]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[PPP1R12A]] | -0.61 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[CEP350]] | -0.60 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.60 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[SHOC2]] | -0.59 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[NDUFC1]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ARID4A]] | -0.58 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[ATOSA]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[SMIM14]] | -0.57 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[ARF5]] | -0.57 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[RPS27L]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGSF9B]] | B | IGSF9B activity raises SLC19A1's level | lines that do not express IGSF9B (17) vs lines expressing it (33) | 1.31× lower at baseline in the lines without IGSF9B | 0.019 | ⚠ within organs, on part of the lines; also absent: ADRA2C, PTPRN2, CBFA2T3 |
| [[GNAZ]] | B | GNAZ activity raises SLC19A1's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.36× lower at baseline in the lines without GNAZ | 0.064 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises SLC19A1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DUXAP9]] | B | DUXAP9 activity raises SLC19A1's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without DUXAP9 | 0.074 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[LDLRAD3]] | B | LDLRAD3 activity raises SLC19A1's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.60× lower at baseline in the lines without LDLRAD3 | 0.091 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.1, -38.6); signed map (-7.3, -54.8). **Vector** length 76.3, 12.7% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +8.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +6.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -9.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.2 | -4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.2 | -13.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -2.5 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 19 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:45,493,572-45,573,365 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FOLT, RFC1, IFC-1, RFC, hRFC, RFT-1 |
| Gene groups (HGNC) | Minor histocompatibility antigens; Solute carrier family 19 |
| Hallmark sets | MYC_TARGETS_V2, ADIPOGENESIS |
| Reactome | 3 pathways, smallest: Metabolism of folate and pterines; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P41440](https://www.uniprot.org/uniprotkb/P41440) (Reduced folate transporter):

> Antiporter that mediates the import of reduced folates or a subset of cyclic dinucleotides, driven by the export of organic anions. Acts as an importer of immunoreactive cyclic dinucleotides, such as cyclic GMP-AMP (2'-3'-cGAMP), an immune messenger produced in response to DNA virus in the cytosol, and its linkage isomer 3'-3'-cGAMP, thus playing a role in triggering larger immune responses. Mechanistically, acts as a secondary active transporter, which exports intracellular organic anions down …

**Summary**, from NCBI Gene [6573](https://www.ncbi.nlm.nih.gov/gene/6573):

> The membrane protein encoded by this gene is a transporter of folate and is involved in the regulation of intracellular concentrations of folate. Three transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:10937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10937) · Entrez [6573](https://www.ncbi.nlm.nih.gov/gene/6573) · UniProt [P41440](https://www.uniprot.org/uniprotkb/P41440) · Ensembl [ENSG00000173638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173638)

## Data

Gene col 10412: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10412); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10412, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10412]; `tensor/DDL_lfc|DDL_z.npy` [10412]; `embed/gene_vectors.npy` [10412]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10412 or target_col == 10412). Every well: [[SLC19A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC19A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
