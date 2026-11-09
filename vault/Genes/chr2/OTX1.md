---
symbol: "OTX1"
type: "gene"
col: 3685
ensembl_id: "ENSG00000115507"
name: "orthodenticle homeobox 1"
location: "2p15"
module: 30
arm: "+"
pooled_cpm: 2.47
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# OTX1

*orthodenticle homeobox 1* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.87× (z +5.7, q 5e-06, up in 17 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.322× (z -10.1, q 3e-21, down in 27 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XKR8]] (+0.78, fdr 7e-06), [[DUSP9]] (+0.66, fdr 1e-05), [[POMGNT2]] (+0.65, fdr 1e-05); moves opposite to [[SDCBP2-AS1]] (-0.61, fdr 3e-05), [[RAB30-DT]] (-0.61, fdr 7e-05), [[MSRA]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +5.7 | 5e-06 | 17/43 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +5.4 | 2e-05 | 17/44 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +4.8 | 2e-04 | 0/2 | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.37×** | +4.1 | 0.007 | 4/42 (A-427, SW1417, …) | top dose only | low cells (technical?); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +4.0 | 0.007 | 3/14 (HEC-1-A, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.007 | 5/25 (A-172, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +3.7 | 0.016 | 6/44 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.064 | 7/43 (NCI-H2030, NCI-H1792, …) | rises with dose | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | 1.39× | +3.0 | 0.15 | 5/26 (PANC-1, RKO, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3685.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.322×** | -10.1 | 3e-21 | 27/40 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.346×** | -9.8 | 2e-20 | 24/45 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.464×** | -7.1 | 2e-10 | 23/40 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.609×** | -6.5 | 9e-09 | 20/31 (A498, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.569×** | -5.2 | 2e-05 | 17/40 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.569×** | -5.2 | 2e-05 | 14/35 (SHP-77, KATO III, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -4.9 | 7e-05 | 9/20 (PANC-1, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.458×** | -3.8 | 0.011 | 11/37 (A498, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -3.5 | 0.025 | 14/41 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.693×** | -3.4 | 0.035 | 14/44 (SW 900, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -3.2 | 0.062 | 11/32 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.709×** | -3.2 | 0.062 | 8/38 (A-172, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.93 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -17.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0671× (z -11.9) |
| [[LoVo (line)]] | wt | 3.16 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0957× (z -8.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 3.47 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0842× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 3.40 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0806× (z -10.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 1.41 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0634× (z -9.0) |
| [[A-172 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.874 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.671 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XKR8]] | +0.78 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[DUSP9]] | +0.66 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[POMGNT2]] | +0.65 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[HYKK]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.62 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[TADA1]] | +0.62 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.62 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ZNF174]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[C1orf174]] | +0.61 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[SLC9A6]] | +0.60 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[SYBU]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[RGS14]] | +0.59 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP2-AS1]] | -0.61 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[RAB30-DT]] | -0.61 | -0.38 / -0.62 | both halves | 7e-05 |  |
| [[MSRA]] | -0.60 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[R3HDM2]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[TSGA10]] | -0.58 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ERCC6L2]] | -0.58 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[RGS5]] | -0.57 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ALG13]] | -0.57 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[TUG1]] | -0.56 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[ZNF655]] | -0.56 | -0.28 / -0.60 | both halves | 3e-04 |  |
| [[PDCL3P4]] | -0.55 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[APLF]] | -0.55 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers OTX1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers OTX1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-0.5, -4.2); signed map (-35.8, -4.2). **Vector** length 47.2, 5.69% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +2.3 | +4.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.6 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.0 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -10.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.3 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | orthodenticle homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:63,050,057-63,057,836 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Orthodenticle homeobox family |
| Matched by | ensembl_id |

**Function**, from UniProt [P32242](https://www.uniprot.org/uniprotkb/P32242) (Homeobox protein OTX1):

> Probably plays a role in the development of the brain and the sense organs. Can bind to the BCD target sequence (BTS): 5'-TCTAATCCC-3'.

**Summary**, from NCBI Gene [5013](https://www.ncbi.nlm.nih.gov/gene/5013):

> This gene encodes a member of the bicoid sub-family of homeodomain-containing transcription factors. The encoded protein acts as a transcription factor and may play a role in brain and sensory organ development. A similar protein in mouse is required for proper brain and sensory organ development and can cause epilepsy. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:8521](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8521) · Entrez [5013](https://www.ncbi.nlm.nih.gov/gene/5013) · UniProt [P32242](https://www.uniprot.org/uniprotkb/P32242) · Ensembl [ENSG00000115507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115507)

## Data

Gene col 3685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3685); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3685]; `tensor/DDL_lfc|DDL_z.npy` [3685]; `embed/gene_vectors.npy` [3685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3685 or target_col == 3685). Every well: [[OTX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
