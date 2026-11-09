---
symbol: "UBQLN4"
type: "gene"
col: 8385
ensembl_id: "ENSG00000160803"
name: "ubiquilin 4"
location: "1q22"
module: 126
arm: "+"
pooled_cpm: 15.07
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# UBQLN4

*ubiquilin 4* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.36× (z +12.0, q 1e-30, up in 21 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.92× (z +9.5, q 5e-19, up in 28 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0929×); [[Saquinavir (drug)]] 0.5 µM in 1 line (Hs 766T 0.102×); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HS-578T 0.110×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[U2AF2]] (+0.73, fdr 2e-05), [[KLC2]] (+0.73, fdr 7e-06), [[DHFR]] (+0.72, fdr 3e-05); moves opposite to [[TMEM191A-1]] (-0.66, fdr 7e-05), [[PITPNA-AS1]] (-0.66, fdr 5e-05), [[CTR9]] (-0.65, fdr 1e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +12.0 | 1e-30 | 21/25 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +9.9 | 1e-20 | 36/40 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +9.5 | 5e-19 | 28/46 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.1 | 2e-10 | 30/45 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +6.5 | 1e-08 | 23/32 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +4.8 | 1e-04 | 26/46 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +4.7 | 2e-04 | 25/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.3 | 9e-04 | 25/43 (SNU-423, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +4.3 | 9e-04 | 24/47 (NCI-H460, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.0 | 0.004 | 19/41 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.42×** | +3.6 | 0.018 | 15/46 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.059 | 17/46 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.075 | 8/46 (RPMI-7951, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.076 | 19/46 (HOP62, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.076 | 11/46 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8385.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0929×); [[Saquinavir (drug)]] 0.5 µM in 1 line (Hs 766T 0.102×); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HS-578T 0.110×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | 0.801× | -3.3 | 0.35 | 11/48 (A-172, SHP-77, …) | top dose only | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.735× | -3.2 | 0.35 | 14/47 (HepG2/C3A, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 2 | — | [[Saquinavir (drug)]] 0.5 µM 0.102× (z -10.6) |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 2 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.110× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 14.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.02× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 9.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0929× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 15.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.11× (z +8.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.163× (z -9.1) |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.105× (z -9.0) |
| [[SNU-423 (line)]] | alt | 7.88 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0965× (z -9.2) |
| [[A-172 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[U2AF2]] | +0.73 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[KLC2]] | +0.73 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[DHFR]] | +0.72 | +0.45 / +0.77 | both halves | 3e-05 |  |
| [[RCN1]] | +0.71 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[CAPRIN1]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[EEF1A1]] | +0.71 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[RCC2]] | +0.70 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[CERS2]] | +0.70 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[MOB1A]] | +0.67 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[IPO5]] | +0.66 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[CTSZ]] | +0.65 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[EEF1A1P5]] | +0.65 | +0.50 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM191A-1]] | -0.66 | -0.37 / -0.68 | both halves | 7e-05 |  |
| [[PITPNA-AS1]] | -0.66 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[CTR9]] | -0.65 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[IMP3]] | -0.64 | -0.50 / -0.66 | both halves | 1e-05 | STRING 451 |
| [[NOSIP]] | -0.64 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.63 | -0.37 / -0.68 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | -0.63 | -0.41 / -0.65 | both halves | 4e-05 | STRING 467; ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC2B]] | -0.62 | -0.41 / -0.75 | both halves | 4e-05 |  |
| [[ADPRS]] | -0.62 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[ISCA2]] | -0.62 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[LAMTOR5]] | -0.61 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[C19orf81]] | -0.61 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[OCEL1]] | -0.61 | -0.33 / -0.62 | both halves | 1e-04 |  |
| [[SF3B6]] | -0.61 | -0.37 / -0.59 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UBQLN4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KCTD15]] | B | KCTD15 activity raises UBQLN4's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without KCTD15 | 0.091 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |
| [[NCS1]] | B | NCS1 activity raises UBQLN4's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without NCS1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.9, -23.7); signed map (-13.0, -36.3). **Vector** length 94.9, 20.5% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.1 | +4.3 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.8 | +2.9 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +1.8 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.7 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | +0.1 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ubiquilin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,035,299-156,053,798 (-) |
| Ensembl biotype | protein_coding |
| Also known as | A1U, UBIN, CIP75; previously C1orf6 |
| Gene groups (HGNC) | Ubiquilin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRR5](https://www.uniprot.org/uniprotkb/Q9NRR5) (Ubiquilin-4):

> Regulator of protein degradation that mediates the proteasomal targeting of misfolded, mislocalized or accumulated proteins. Acts by binding polyubiquitin chains of target proteins via its UBA domain and by interacting with subunits of the proteasome via its ubiquitin-like domain. Key regulator of DNA repair that represses homologous recombination repair: in response to DNA damage, recruited to sites of DNA damage following phosphorylation by ATM and acts by binding and removing ubiquitinated …

**Summary**, from NCBI Gene [56893](https://www.ncbi.nlm.nih.gov/gene/56893):

> Enables K48-linked polyubiquitin modification-dependent protein binding activity and identical protein binding activity. Involved in several processes, including negative regulation of autophagosome maturation; negative regulation of double-strand break repair via homologous recombination; and regulation of proteasomal ubiquitin-dependent protein catabolic process. Located in several cellular components, including autophagosome; proteasome complex; and site of DNA damage. Part of …

**Accessions** — [HGNC:1237](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1237) · Entrez [56893](https://www.ncbi.nlm.nih.gov/gene/56893) · UniProt [Q9NRR5](https://www.uniprot.org/uniprotkb/Q9NRR5) · Ensembl [ENSG00000160803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160803)

## Data

Gene col 8385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8385); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8385]; `tensor/DDL_lfc|DDL_z.npy` [8385]; `embed/gene_vectors.npy` [8385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8385 or target_col == 8385). Every well: [[UBQLN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBQLN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
