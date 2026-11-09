---
symbol: "CDNF"
type: "gene"
col: 11650
ensembl_id: "ENSG00000185267"
name: "cerebral dopamine neurotrophic factor"
location: "10p13"
module: 15
arm: "+"
pooled_cpm: 2.2
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 10
n_dd_up_clean: 17
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CDNF

*cerebral dopamine neurotrophic factor* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.87× (z +27.3, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.389× (z -8.4, q 3e-14, down in 26 of 44 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.439× (z -6.1, q 2e-07, down in 21 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPESP1]] (+0.75, fdr 1e-05), [[MYLK4]] (+0.75, fdr 1e-05), [[SEC24B-AS1]] (+0.73, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11650.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.87×** | +27.3 | 0e+00 | 32/32 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.53×** | +12.9 | 2e-35 | 19/23 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +10.3 | 1e-22 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.95×** | +9.2 | 5e-18 | 20/30 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.82×** | +7.5 | 8e-12 | 10/43 (RKO, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.7 | 2e-09 | 9/43 (A498, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +6.3 | 2e-08 | 1/3 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +5.6 | 2e-06 | 3/10 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.82×** | +5.2 | 1e-05 | 12/42 (KATO III, SW48, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +4.0 | 0.003 | 5/44 (A498, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.009 | 6/43 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +3.7 | 0.010 | 4/44 (LS 180, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.36×** | +3.7 | 0.010 | 3/43 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.50×** | +3.6 | 0.014 | 2/44 (NCI-H2030, KATO III) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.016 | 10/40 (A-172, HOP62, …) | top dose only |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.044 | 3/35 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.045 | 5/24 (SW480, NCI-H2030, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.44×** | +3.2 | 0.045 | 5/37 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.052 | 1/43 (NCI-H460) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11650.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.389×** | -8.4 | 3e-14 | 26/44 (C-33 A, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.393×** | -8.2 | 5e-14 | 24/45 (Hs 766T, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.439×** | -6.1 | 2e-07 | 21/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.517×** | -5.8 | 8e-07 | 14/23 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.539×** | -4.6 | 5e-04 | 14/40 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.546×** | -3.8 | 0.012 | 7/44 (MIA PaCa-2, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.740×** | -3.8 | 0.012 | 14/41 (SNU-1, PANC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.676×** | -3.5 | 0.034 | 12/45 (HepG2/C3A, SW 900, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.478×** | -3.4 | 0.039 | 11/31 (LS 180, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.646×** | -3.3 | 0.065 | 13/39 (A-427, SW480, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.699× | -3.1 | 0.11 | 3/44 (H4, NCI-H23, …) | top dose only |  |
| [[Hesperidin (drug)]] 0.05 µM |  | 0.691× | -3.0 | 0.11 | 6/40 (NCI-H2030, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 1.84 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.69× (z +10.0) | [[Harringtonine (drug)]] 5 µM 0.0285× (z -11.2) ⚠ cell-cycle shift, explains ~96% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0332× (z -9.3) |
| [[SW480 (line)]] | alt | 2.22 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.39× (z +10.3) | [[Digitoxin (drug)]] 0.5 µM 0.0447× (z -9.0) |
| [[A-172 (line)]] | wt | 1.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +9.4) | — |
| [[A498 (line)]] | wt | 2.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.00× (z +9.1) | — |
| [[A549 (line)]] | wt | 1.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.5× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 2.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 3.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 2.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +8.8) | — |
| [[LoVo (line)]] | wt | 2.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.14× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 5.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 2.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.74× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 3.51 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.89× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 2.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.32× (z +10.0) | — |
| [[SW1417 (line)]] | alt | 2.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +10.2) | — |
| [[A-427 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPESP1]] | +0.75 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[MYLK4]] | +0.75 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[SEC24B-AS1]] | +0.73 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ALG1L9P]] | +0.73 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[DICER1-AS1]] | +0.73 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[PJVK]] | +0.73 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[CRTC3-AS1]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[FAM174B]] | +0.73 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[INTS6-AS1]] | +0.72 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[KCTD21-AS1]] | +0.72 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[SIAH2-AS1]] | +0.71 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[IDNK]] | +0.71 | +0.66 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDNF's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TMCC1-DT]] | C | TMCC1-DT activity raises CDNF's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 1.47× lower at baseline in the lines without TMCC1-DT | 0.063 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (3.7, 22.0); signed map (31.9, -8.1). **Vector** length 47.7, 6.19% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +27.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +5.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +3.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.1 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -8.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.3 | +3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | +3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.8 | +3.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.8 | +4.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | +0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +2.6 |

## What is on record

|  |  |
|---|---|
| Name | cerebral dopamine neurotrophic factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:14,819,245-14,838,575 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ARMETL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q49AH0](https://www.uniprot.org/uniprotkb/Q49AH0) (Cerebral dopamine neurotrophic factor):

> Trophic factor for dopamine neurons. Prevents the 6-hydroxydopamine (6-OHDA)-induced degeneration of dopaminergic neurons. When administered after 6-OHDA-lesioning, restores the dopaminergic function and prevents the degeneration of dopaminergic neurons in substantia nigra (By similarity).

**Summary**, from NCBI Gene [441549](https://www.ncbi.nlm.nih.gov/gene/441549):

> Predicted to enable growth factor activity. Predicted to be involved in dopaminergic neuron differentiation and neuron projection development. Predicted to act upstream of or within developmental process. Predicted to be located in extracellular region. Predicted to be active in endoplasmic reticulum and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24913) · Entrez [441549](https://www.ncbi.nlm.nih.gov/gene/441549) · UniProt [Q49AH0](https://www.uniprot.org/uniprotkb/Q49AH0) · Ensembl [ENSG00000185267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185267)

## Data

Gene col 11650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11650); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11650]; `tensor/DDL_lfc|DDL_z.npy` [11650]; `embed/gene_vectors.npy` [11650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11650 or target_col == 11650). Every well: [[CDNF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDNF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
