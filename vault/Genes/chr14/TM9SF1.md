---
symbol: "TM9SF1"
type: "gene"
col: 2045
ensembl_id: "ENSG00000100926"
name: "transmembrane 9 superfamily member 1"
location: "14q12"
module: 42
arm: "+"
pooled_cpm: 17.83
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TM9SF1

*transmembrane 9 superfamily member 1* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.76× (z +8.7, q 2e-15, up in 21 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.39× (z +3.8, q 0.019, up in 14 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.415× (z -14.1, q 4e-42, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TM9SF4]] (+0.54, fdr 4e-05), [[SLC39A9]] (+0.53, fdr 1e-05), [[ZZEF1]] (+0.52, fdr 1e-05); moves opposite to [[AFDN]] (-0.52, fdr 4e-04), [[RAC1]] (-0.49, fdr 4e-04), [[FGD6]] (-0.48, fdr 1e-04).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +8.7 | 2e-15 | 21/31 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +7.3 | 9e-11 | 0/48 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +5.7 | 3e-06 | 22/39 (Panc 03.27, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **1.29×** | +4.1 | 0.006 | 16/44 (A-427, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.019 | 14/47 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.15× | +3.1 | 0.17 | 11/48 (Hs 766T, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2045.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.415×** | -14.1 | 4e-42 | 45/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.427×** | -13.6 | 1e-39 | 47/48 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.443×** | -13.0 | 2e-36 | 43/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.542×** | -9.8 | 2e-20 | 42/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.697×** | -8.2 | 3e-14 | 30/47 (hTERT-HPNE, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.733×** | -7.0 | 2e-10 | 32/48 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.655×** | -6.5 | 6e-09 | 26/47 (NCI-H23, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.678×** | -6.2 | 4e-08 | 24/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.672×** | -6.1 | 6e-08 | 29/47 (NCI-H23, NCI-H2030, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.707×** | -5.5 | 2e-06 | 24/47 (KATO III, H4, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.785×** | -5.5 | 2e-06 | 25/46 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.720×** | -5.3 | 7e-06 | 26/48 (KATO III, SW48, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.551×** | -5.0 | 3e-05 | 25/48 (NCI-H460, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -4.3 | 7e-04 | 22/46 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.766×** | -4.3 | 8e-04 | 19/46 (HT-29, C-33 A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.783×** | -3.9 | 0.003 | 15/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 20.4 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.272× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -15.8) |
| [[LoVo (line)]] | wt | 16.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.302× (z -9.2) |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.0896× (z -8.6) |
| [[SW480 (line)]] | alt | 15.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.351× (z -8.7) |
| [[A-172 (line)]] | wt | 14.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -10.1) |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 30.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -12.5) |
| [[H4 (line)]] | wt | 26.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.187× (z -9.5) |
| [[LS 180 (line)]] | wt | 14.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.249× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -9.7) |
| [[RKO (line)]] | wt | 17.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -11.8) |
| [[SW48 (line)]] | wt | 15.7 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0688× (z -11.4) |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM9SF4]] | +0.54 | +0.41 / +0.58 | both halves | 4e-05 | same gene group |
| [[SLC39A9]] | +0.53 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ZZEF1]] | +0.52 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[TMED1]] | +0.52 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[LMAN2]] | +0.51 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CNOT3]] | +0.51 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[SLC35A2]] | +0.51 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[LSM1]] | +0.51 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[RFX1]] | +0.50 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[CTDNEP1]] | +0.50 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[HSPA13]] | +0.50 | +0.54 / +0.37 | both halves | 7e-05 |  |
| [[ZNF576]] | +0.50 | +0.39 / +0.58 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFDN]] | -0.52 | -0.26 / -0.52 | both halves | 4e-04 |  |
| [[RAC1]] | -0.49 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[FGD6]] | -0.48 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[FMNL2]] | -0.48 | -0.34 / -0.30 | both halves | 2e-04 |  |
| [[SMS]] | -0.47 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[MBOAT2]] | -0.45 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[FLNB]] | -0.45 | -0.13 / -0.37 | ⚠ not reproduced | 0.002 |  |
| [[RASA2]] | -0.44 | -0.27 / -0.28 | both halves | 3e-04 |  |
| [[RHOF]] | -0.42 | -0.33 / -0.25 | both halves | 4e-04 |  |
| [[IGSF9B]] | -0.42 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[RAP1GAP2]] | -0.42 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[VEZT]] | -0.41 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[LPCAT2]] | -0.41 | -0.26 / -0.33 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TM9SF1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.287). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.7, -55.8); signed map (-58.8, 13.3). **Vector** length 54.5, 7.63% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | -8.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +0.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -7.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.2 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -3.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.1 | -9.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane 9 superfamily member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,189,149-24,195,687 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MP70, HMP70 |
| Gene groups (HGNC) | Transmembrane 9 superfamily members |
| Matched by | ensembl_id |

**Function**, from UniProt [O15321](https://www.uniprot.org/uniprotkb/O15321) (Transmembrane 9 superfamily member 1):

> Plays an essential role in autophagy.

**Summary**, from NCBI Gene [10548](https://www.ncbi.nlm.nih.gov/gene/10548):

> Predicted to be involved in protein localization to membrane. Predicted to be located in autophagosome membrane; cytoplasmic vesicle; and lysosomal membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11864) · Entrez [10548](https://www.ncbi.nlm.nih.gov/gene/10548) · UniProt [O15321](https://www.uniprot.org/uniprotkb/O15321) · Ensembl [ENSG00000100926](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100926)

## Data

Gene col 2045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2045); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2045]; `tensor/DDL_lfc|DDL_z.npy` [2045]; `embed/gene_vectors.npy` [2045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2045 or target_col == 2045). Every well: [[TM9SF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM9SF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
