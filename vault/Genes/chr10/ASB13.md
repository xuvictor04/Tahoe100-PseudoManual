---
symbol: "ASB13"
type: "gene"
col: 12192
ensembl_id: "ENSG00000196372"
name: "ankyrin repeat and SOCS box containing 13"
location: "10p15.1"
module: 33
arm: "+"
pooled_cpm: 5.96
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# ASB13

*ankyrin repeat and SOCS box containing 13* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.59× (z +5.4, q 3e-05, up in 19 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.259× (z -22.1, q 0e+00, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM177]] (+0.79, fdr 7e-06), [[FXN]] (+0.79, fdr 7e-06), [[ANGEL1]] (+0.78, fdr 7e-06); moves opposite to [[USP11]] (-0.62, fdr 1e-05), [[UBE2A]] (-0.59, fdr 3e-05), [[C6orf62]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12192.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +5.4 | 3e-05 | 19/46 (SW480, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.5 | 0.002 | 15/46 (CFPAC-1, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.047 | 3/46 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.084 | 9/44 (A498, A549, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.33× | +3.3 | 0.10 | 9/43 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.32× | +3.3 | 0.10 | 9/44 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.22× | +3.2 | 0.10 | 3/46 (HOP62, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12192.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.259×** | -22.1 | 0e+00 | 40/41 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.442×** | -13.3 | 4e-38 | 32/41 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.303×** | -13.3 | 7e-38 | 34/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.357×** | -11.9 | 2e-30 | 34/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.371×** | -11.4 | 7e-28 | 32/43 (NCI-H2030, J82, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.408×** | -9.9 | 2e-21 | 25/35 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.462×** | -8.9 | 4e-17 | 33/47 (MIA PaCa-2, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.475×** | -8.1 | 4e-14 | 29/42 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.492×** | -7.9 | 2e-13 | 27/40 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -7.8 | 2e-13 | 25/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -7.5 | 3e-12 | 25/45 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.532×** | -7.3 | 1e-11 | 26/44 (HT-29, SW48, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.358×** | -6.2 | 3e-08 | 23/44 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.599×** | -5.9 | 2e-07 | 21/44 (C-33 A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -5.6 | 1e-06 | 22/40 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.744×** | -4.8 | 5e-05 | 21/46 (SW480, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12192. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.95 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0352× (z -25.3) |
| [[PANC-1 (line)]] | alt | 5.46 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0594× (z -23.4) |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0651× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0803× (z -11.4) |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0788× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.114× (z -11.2) |
| [[SNU-1 (line)]] | wt | 18.5 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0721× (z -10.1) |
| [[SW480 (line)]] | alt | 8.29 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 9.12 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0740× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.191× (z -13.4) |
| [[LoVo (line)]] | wt | 6.56 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0863× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -9.7) |
| [[SW1417 (line)]] | alt | 9.34 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -14.0) |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -11.6) |
| [[C32 (line)]] | wt | 3.88 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0270× (z -10.0) |
| [[J82 (line)]] | alt | 7.76 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 8.14 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -14.0) |
| [[SW48 (line)]] | wt | 13.7 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.0600× (z -10.4) |
| [[A498 (line)]] | wt | 6.60 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0513× (z -21.5) |
| [[A549 (line)]] | wt | 6.12 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0597× (z -16.9) |
| [[HepG2_C3A (line)]] | wt | 7.70 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0595× (z -9.8) |
| [[HOP62 (line)]] | alt | 4.07 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0382× (z -11.7) |
| [[HT-29 (line)]] | alt | 5.78 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0543× (z -11.3) |
| [[COLO 205 (line)]] | alt | 9.30 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0405× (z -10.4) |
| [[KATO III (line)]] | alt | 5.86 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0666× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 7.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0686× (z -11.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 4.01 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0933× (z -10.5) |
| [[A-172 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12192), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM177]] | +0.79 | +0.62 / +0.79 | both halves | 7e-06 |  |
| [[FXN]] | +0.79 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[ANGEL1]] | +0.78 | +0.65 / +0.84 | both halves | 7e-06 |  |
| [[NLE1]] | +0.73 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[RSAD1]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ZNF692]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.69 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[ZFAND4]] | +0.69 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SCAP]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CHST10]] | +0.68 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[BRAT1]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP11]] | -0.62 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[UBE2A]] | -0.59 | -0.43 / -0.54 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[C6orf62]] | -0.58 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[CCNT2-AS1]] | -0.58 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[LINC02955]] | -0.58 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ATXN1L]] | -0.57 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CCDC200]] | -0.57 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[FAM151B]] | -0.57 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[TSPAN31]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[LINC00310]] | -0.57 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ASB13's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MCOLN2]] | B | MCOLN2 activity raises ASB13's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.01× lower at baseline in the lines without MCOLN2 | 0.098 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.7, -40.8); signed map (-8.3, -53.1). **Vector** length 78.1, 14.8% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.51 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.51 to 10); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.53 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -13.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -22.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -7.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and SOCS box containing 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:5,638,867-5,666,595 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13134, MGC19879 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXK3](https://www.uniprot.org/uniprotkb/Q8WXK3) (Ankyrin repeat and SOCS box protein 13):

> May be a substrate-recognition component of a SCF-like ECS (Elongin-Cullin-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins.

**Summary**, from NCBI Gene [79754](https://www.ncbi.nlm.nih.gov/gene/79754):

> The protein encoded by this gene is a member of the ankyrin repeat and SOCS box-containing (ASB) family of proteins. They contain ankyrin repeat sequence and a SOCS box domain. The SOCS box serves to couple suppressor of cytokine signalling (SOCS) proteins and their binding partners with the elongin B and C complex, possibly targeting them for degradation. Multiple alternatively spliced transcript variants, both protein-coding and not protein-coding, have been described for this gene. [provided …

**Accessions** — [HGNC:19765](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19765) · Entrez [79754](https://www.ncbi.nlm.nih.gov/gene/79754) · UniProt [Q8WXK3](https://www.uniprot.org/uniprotkb/Q8WXK3) · Ensembl [ENSG00000196372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196372)

## Data

Gene col 12192: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12192); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12192, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12192]; `tensor/DDL_lfc|DDL_z.npy` [12192]; `embed/gene_vectors.npy` [12192]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12192 or target_col == 12192). Every well: [[ASB13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASB13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
