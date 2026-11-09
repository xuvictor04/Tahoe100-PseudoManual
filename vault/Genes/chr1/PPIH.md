---
symbol: "PPIH"
type: "gene"
col: 10190
ensembl_id: "ENSG00000171960"
name: "peptidylprolyl isomerase H"
location: "1p34.2"
module: 71
arm: "+"
pooled_cpm: 25.38
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# PPIH

*peptidylprolyl isomerase H* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.57× (z +7.2, q 3e-10, up in 30 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Sapanisertib (drug)]] 0.5 µM: 1.40× (z +3.8, q 0.007, up in 16 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.709× (z -7.8, q 3e-12, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUP85]] (+0.79, fdr 7e-06), [[MTBP]] (+0.79, fdr 7e-06), [[RFC4]] (+0.75, fdr 7e-06); moves opposite to [[SDCBP]] (-0.61, fdr 1e-05), [[LACC1]] (-0.58, fdr 3e-05), [[TSPAN31]] (-0.57, fdr 1e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LACC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10190.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.57×** | +7.2 | 3e-10 | 30/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **1.49×** | +6.4 | 5e-08 | 21/42 (NCI-H460, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.50×** | +6.2 | 1e-07 | 18/36 (A-172, AsPC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.51×** | +6.1 | 2e-07 | 24/40 (A-172, LS 180, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +5.3 | 1e-05 | 28/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.38×** | +4.9 | 7e-05 | 24/46 (J82, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.35×** | +4.7 | 2e-04 | 21/47 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.33×** | +4.6 | 3e-04 | 19/47 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **1.34×** | +4.5 | 4e-04 | 21/44 (NCI-H2030, J82, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.33×** | +4.5 | 4e-04 | 23/45 (A-172, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.29×** | +4.1 | 0.002 | 15/48 (SW480, LS 180, …) | all doses, flat | composition shift |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.40×** | +3.8 | 0.007 | 16/48 (NCI-H23, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.26×** | +3.7 | 0.009 | 17/45 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.6 | 0.015 | 9/28 (HOP62, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.25×** | +3.5 | 0.015 | 17/48 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.35×** | +3.4 | 0.021 | 12/48 (NCI-H460, PANC-1, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.029 | 14/47 (LOX-IMVI, SNU-1, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.060 | 13/45 (RPMI-7951, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10190.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.709×** | -7.8 | 3e-12 | 30/48 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.764×** | -6.1 | 3e-07 | 32/48 (COLO 205, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.691×** | -5.9 | 6e-07 | 28/47 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.790×** | -3.7 | 0.030 | 15/47 (A-427, COLO 205, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.853× | -3.6 | 0.030 | 16/48 (KATO III, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.859× | -3.5 | 0.048 | 18/48 (MIA PaCa-2, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.827× | -3.1 | 0.13 | 13/47 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.827× | -3.1 | 0.13 | 13/48 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.827× | -3.1 | 0.13 | 7/47 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 27.0 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.276× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.9) |
| [[AN3 CA (line)]] | alt | 44.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.5) |
| [[H4 (line)]] | wt | 33.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.7) |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 18.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | — |
| [[SW480 (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.31× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | — |
| [[A-172 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP85]] | +0.79 | +0.75 / +0.78 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MTBP]] | +0.79 | +0.81 / +0.77 | both halves | 7e-06 |  |
| [[RFC4]] | +0.75 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[ZNF519]] | +0.73 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[TRAIP]] | +0.71 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[NDC1]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[SNRNP40]] | +0.69 | +0.73 / +0.63 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 928 |
| [[SASS6]] | +0.69 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[TOPBP1]] | +0.68 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[NUP160]] | +0.68 | +0.73 / +0.58 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[RAD51]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[THOC3]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP]] | -0.61 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[LACC1]] | -0.58 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[TSPAN31]] | -0.57 | -0.60 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LACC1]] | B | LACC1 activity lowers PPIH's level | lines that do not express LACC1 (6) vs lines expressing it (44) | 1.52× higher at baseline in the lines without LACC1 | 0.038 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[PBK]] | C | PBK activity raises PPIH's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without PBK | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.715). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.9, -48.2); signed map (-40.5, -41.7). **Vector** length 78.4, 16.9% of its response variance represented; |z| ≥ 3 in 699 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IP3 and IP4 transport between cytosol and nucleus* (reactome, mean cos +0.52 to 4); *IP6 and IP7 transport between cytosol and nucleus* (reactome, mean cos +0.52 to 4); *IPs transport between nucleus and cytosol* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +5.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +2.4 | +4.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | +2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.7 | +3.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.7 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.1 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:42,658,335-42,676,758 (+) |
| Ensembl biotype | protein_coding |
| Also known as | USA-CYP, CYP-20, SnuCyp-20, CYPH, MGC5016 |
| Gene groups (HGNC) | Cyclophilin peptidylprolyl isomerases; U4/U6 small nuclear ribonucleoprotein particle |
| Reactome | 9 pathways, smallest: SARS-CoV-1 activates/modulates innate immune responses; SARS-CoV-1-host interactions; SARS-CoV-1 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [O43447](https://www.uniprot.org/uniprotkb/O43447) (Peptidyl-prolyl cis-trans isomerase H):

> PPIase that catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and may therefore assist protein folding. Participates in pre-mRNA splicing. May play a role in the assembly of the U4/U5/U6 tri-snRNP complex, one of the building blocks of the spliceosome. May act as a chaperone.

**Summary**, from NCBI Gene [10465](https://www.ncbi.nlm.nih.gov/gene/10465):

> The protein encoded by this gene is a member of the peptidyl-prolyl cis-trans isomerase (PPIase) family. PPIases catalyze the cis-trans isomerization of proline imidic peptide bonds in oligopeptides and accelerate the folding of proteins. This protein is a specific component of the complex that includes pre-mRNA processing factors PRPF3, PRPF4, and PRPF18, as well as U4/U5/U6 tri-snRNP. This protein has been shown to possess PPIase activity and may act as a protein chaperone that mediates the …

**Accessions** — [HGNC:14651](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14651) · Entrez [10465](https://www.ncbi.nlm.nih.gov/gene/10465) · UniProt [O43447](https://www.uniprot.org/uniprotkb/O43447) · Ensembl [ENSG00000171960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171960)

## Data

Gene col 10190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10190); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10190]; `tensor/DDL_lfc|DDL_z.npy` [10190]; `embed/gene_vectors.npy` [10190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10190 or target_col == 10190). Every well: [[PPIH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
