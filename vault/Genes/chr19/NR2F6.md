---
symbol: "NR2F6"
type: "gene"
col: 8301
ensembl_id: "ENSG00000160113"
name: "nuclear receptor subfamily 2 group F member 6"
location: "19p13.11"
module: 54
arm: "+"
pooled_cpm: 13.53
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# NR2F6

*nuclear receptor subfamily 2 group F member 6* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.64× (z +4.6, q 0.002, up in 25 of 41 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~34% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.326× (z -14.9, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL34]] (+0.78, fdr 7e-06, ⚠ same locus), [[SAC3D1]] (+0.73, fdr 1e-05), [[ANKRD13D]] (+0.72, fdr 7e-06), [[NFATC3]] (+0.71, fdr 7e-06); moves opposite to [[SLC30A9]] (-0.67, fdr 7e-06), [[ZNF655]] (-0.66, fdr 2e-05), [[SDCBP2-AS1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MNX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.64×** | +4.6 | 0.002 | 25/41 (LS 180, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.8 | 0.035 | 20/41 (SHP-77, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.28× | +3.2 | 0.22 | 17/46 (NCI-H2347, NCI-H661, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.326×** | -14.9 | 0e+00 | 42/46 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.365×** | -9.5 | 8e-19 | 38/44 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.352×** | -9.4 | 8e-19 | 37/45 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.253×** | -5.9 | 6e-07 | 33/46 (NCI-H1792, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.563×** | -5.4 | 8e-06 | 29/46 (NCI-H2030, A-427, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.601×** | -4.8 | 2e-04 | 25/46 (A-427, HT-29, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.618×** | -4.5 | 5e-04 | 21/45 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.360×** | -4.4 | 9e-04 | 24/43 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.702×** | -3.3 | 0.053 | 21/46 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -3.3 | 0.053 | 18/46 (BT-474, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -3.2 | 0.069 | 19/45 (HS-578T, H4, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.489× | -3.0 | 0.11 | 10/45 (SNU-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 23.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -14.8) |
| [[A-427 (line)]] | wt | 31.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0877× (z -14.7) |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -21.2) |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -12.1) |
| [[A-172 (line)]] | wt | 8.64 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -12.8) |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0756× (z -13.0) |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -11.5) |
| [[PANC-1 (line)]] | alt | 16.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -13.2) |
| [[RKO (line)]] | wt | 17.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -10.9) |
| [[A498 (line)]] | wt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -11.7) |
| [[BT-474 (line)]] | alt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.3) |
| [[COLO 205 (line)]] | alt | 9.37 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -9.5) |
| [[H4 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0803× (z -9.1) ⚠ cell-cycle shift, explains ~67% of this change |
| [[Hs 766T (line)]] | wt | 8.95 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -11.4) |
| [[LoVo (line)]] | wt | 9.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 9.84 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.101× (z -10.3) |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.230× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -9.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 10.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 6.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -8.5) |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0610× (z -9.8) |
| [[SW480 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -8.7) |
| [[A549 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL34]] | +0.78 | +0.65 / +0.79 | both halves | 7e-06 | ⚠ same locus (46.7 kb: neighbours can correlate without regulation) |
| [[SAC3D1]] | +0.73 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[ANKRD13D]] | +0.72 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[NFATC3]] | +0.71 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[POP7]] | +0.70 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[SDHAF1]] | +0.70 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[C15orf61]] ⚠ | +0.69 | +0.45 / +0.66 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LSM2]] | +0.67 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[TRIM62]] | +0.66 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[XYLT2]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.65 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[C6orf136]] | +0.65 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[CCDC107]] | +0.65 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[KIAA2013]] | +0.65 | +0.47 / +0.69 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A9]] | -0.67 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[ZNF655]] | -0.66 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[SDCBP2-AS1]] | -0.62 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[CHM]] | -0.60 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[CCDC50]] | -0.60 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[TRMT13]] | -0.60 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CHMP3]] | -0.59 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[IL6ST]] | -0.58 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[PSME3IP1]] | -0.58 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[PRKAR1A]] | -0.58 | -0.29 / -0.60 | both halves | 3e-04 |  |
| [[EIF4G2]] | -0.58 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[NRAS]] | -0.58 | -0.31 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MNX1]] | B | MNX1 activity raises NR2F6's level | lines that do not express MNX1 (11) vs lines expressing it (39) | 1.53× lower at baseline in the lines without MNX1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ABLIM2, CAMSAP3, GRTP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.2, -4.1); signed map (-34.3, 4.2). **Vector** length 73.2, 15.9% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial ribosome-associated quality control* (reactome, mean cos +0.56 to 9); *Mitochondrial translation* (reactome, mean cos +0.56 to 9); *Mitochondrial translation elongation* (reactome, mean cos +0.56 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | -0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | -0.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.0 | +0.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.0 | +2.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 2 group F member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,231,883-17,245,919 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EAR-2, EAR2; previously ERBAL2 |
| Gene groups (HGNC) | Nuclear receptor subfamily 2 group F |
| Reactome | 1 pathways, smallest: Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P10588](https://www.uniprot.org/uniprotkb/P10588) (Nuclear receptor subfamily 2 group F member 6):

> Transcription factor predominantly involved in transcriptional repression. Binds to promoter/enhancer response elements that contain the imperfect 5'-AGGTCA-3' direct or inverted repeats with various spacings which are also recognized by other nuclear hormone receptors. Involved in modulation of hormonal responses. Represses transcriptional activity of the lutropin-choriogonadotropic hormone receptor/LHCGR gene, the renin/REN gene and the oxytocin-neurophysin/OXT gene. Represses the …

**Summary**, from NCBI Gene [2063](https://www.ncbi.nlm.nih.gov/gene/2063):

> Enables DNA-binding transcription factor activity and sequence-specific double-stranded DNA binding activity. Involved in negative regulation of transcription by RNA polymerase II. Located in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7977](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7977) · Entrez [2063](https://www.ncbi.nlm.nih.gov/gene/2063) · UniProt [P10588](https://www.uniprot.org/uniprotkb/P10588) · Ensembl [ENSG00000160113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160113)

## Data

Gene col 8301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8301); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8301]; `tensor/DDL_lfc|DDL_z.npy` [8301]; `embed/gene_vectors.npy` [8301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8301 or target_col == 8301). Every well: [[NR2F6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR2F6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
