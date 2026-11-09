---
symbol: "CRTC3-AS1"
type: "gene"
col: 15230
ensembl_id: "ENSG00000259736"
name: "CRTC3 antisense RNA 1"
location: "15q26.1"
module: 35
arm: "+"
pooled_cpm: 6.44
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# CRTC3-AS1

*CRTC3 antisense RNA 1* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.69× (z +15.2, q 0e+00, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.417× (z -9.5, q 1e-18, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDNF]] (+0.73, fdr 7e-06), [[IDNK]] (+0.66, fdr 1e-05), [[PAXBP1-AS1]] (+0.64, fdr 2e-05); moves opposite to [[PUSL1]] (-0.52, fdr 4e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[INHA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15230.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.69×** | +15.2 | 0e+00 | 39/42 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +7.8 | 1e-12 | 34/47 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +7.4 | 2e-11 | 25/39 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +5.3 | 1e-05 | 12/30 (HEC-1-A, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +4.8 | 2e-04 | 18/46 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +4.7 | 3e-04 | 6/16 (NCI-H2347, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +4.6 | 4e-04 | 17/47 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.51×** | +4.5 | 5e-04 | 13/47 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +4.2 | 0.002 | 15/47 (A498, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.31×** | +4.2 | 0.002 | 13/46 (HT-29, J82, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.005 | 7/47 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.6 | 0.013 | 4/11 (HS-578T, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.019 | 8/45 (KATO III, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.36×** | +3.3 | 0.034 | 8/45 (HEC-1-A, J82, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.035 | 7/46 (HOP62, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15230.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.417×** | -9.5 | 1e-18 | 35/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.524×** | -7.0 | 6e-10 | 24/42 (C-33 A, SHP-77, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.553×** | -6.4 | 2e-08 | 23/45 (BT-474, COLO 205, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.563×** | -6.2 | 6e-08 | 24/46 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.631×** | -5.0 | 6e-05 | 20/45 (LS 180, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.662×** | -4.5 | 7e-04 | 18/47 (RPMI-7951, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.660×** | -4.3 | 0.001 | 19/45 (SW480, COLO 205, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.670×** | -4.2 | 0.002 | 14/36 (SW480, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.685×** | -4.1 | 0.003 | 12/47 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.705×** | -3.8 | 0.010 | 15/47 (BT-474, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.721×** | -3.5 | 0.020 | 19/46 (PANC-1, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.730×** | -3.4 | 0.030 | 12/46 (PANC-1, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.561×** | -3.3 | 0.045 | 8/43 (SK-MEL-2, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15230. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.07 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +10.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.176× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 5.22 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0689× (z -8.7) |
| [[C-33 A (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0912× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 4.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.69× (z +11.7) | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.109× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 4.51 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.106× (z -8.7) |
| [[LS 180 (line)]] | wt | 5.11 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0607× (z -10.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 7.25 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.101× (z -8.8) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 9.62 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.247× (z -8.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 6.49 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0600× (z -9.8) |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0859× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 8.99 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0942× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15230), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDNF]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[IDNK]] | +0.66 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PAXBP1-AS1]] | +0.64 | +0.67 / +0.48 | both halves | 2e-05 | same gene group |
| [[FAM174B]] | +0.64 | +0.67 / +0.32 | both halves | 1e-04 |  |
| [[DDX19A-DT]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[PJVK]] | +0.63 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[TMLHE-AS1]] | +0.62 | +0.58 / +0.49 | both halves | 1e-05 | same gene group |
| [[DEPDC4]] | +0.61 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SUMO2P17]] | +0.61 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[TMEM72-AS1]] | +0.60 | +0.68 / +0.35 | both halves | 1e-04 | same gene group |
| [[DLGAP4-AS1]] | +0.60 | +0.66 / +0.38 | both halves | 7e-05 | same gene group |
| [[H3-3A-DT]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUSL1]] | -0.52 | -0.43 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INHA]] | B | INHA activity raises CRTC3-AS1's level | lines that do not express INHA (11) vs lines expressing it (39) | 1.28× lower at baseline in the lines without INHA | 0.051 | ⚠ within organs, on part of the lines; also absent: OBSL1, KCNK13 |
| [[TOP2A]] | B | TOP2A activity lowers CRTC3-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TMCC1-DT]] | C | TMCC1-DT activity raises CRTC3-AS1's level | lines that do not express TMCC1-DT (3) vs lines expressing it (47) | 1.81× lower at baseline in the lines without TMCC1-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, WWOX, DBNDD1; maybe low, not absent; its own permutation p |
| [[CATSPER2P1]] | C | CATSPER2P1 activity raises CRTC3-AS1's level | lines that do not express CATSPER2P1 (3) vs lines expressing it (47) | 1.51× lower at baseline in the lines without CATSPER2P1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FAM182B, SLFNL1-AS1, ENSG00000287400; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.5, 22.9); signed map (31.8, -4.2). **Vector** length 48.6, 5.94% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +2.7 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.1 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.9 | +4.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -4.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | CRTC3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q26.1 — chr15:90,620,007-90,717,141 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51433) · Entrez [101926895](https://www.ncbi.nlm.nih.gov/gene/101926895) · Ensembl [ENSG00000259736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259736)

## Data

Gene col 15230: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15230); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15230, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15230]; `tensor/DDL_lfc|DDL_z.npy` [15230]; `embed/gene_vectors.npy` [15230]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15230 or target_col == 15230). Every well: [[CRTC3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRTC3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
