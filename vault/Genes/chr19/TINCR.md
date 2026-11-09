---
symbol: "TINCR"
type: "gene"
col: 13350
ensembl_id: "ENSG00000223573"
name: "TINCR ubiquitin domain containing"
location: "19p13.3"
module: 38
arm: "+"
pooled_cpm: 7.42
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 15
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# TINCR

*TINCR ubiquitin domain containing* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.14× (z +16.4, q 0e+00, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.553× (z -5.8, q 4e-06, down in 23 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM41]] (+0.82, fdr 7e-06), [[RFPL3S]] (+0.80, fdr 7e-06), [[CPNE9]] (+0.80, fdr 7e-06); moves opposite to [[PPP2R1B]] (-0.61, fdr 1e-05), [[RPE]] (-0.61, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.14×** | +16.4 | 0e+00 | 37/44 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +6.8 | 3e-09 | 18/40 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +6.6 | 8e-09 | 29/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +6.0 | 3e-07 | 20/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +5.9 | 4e-07 | 27/46 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +4.5 | 6e-04 | 23/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.008 | 17/43 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.008 | 16/47 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.91×** | +3.4 | 0.039 | 9/39 (LOX-IMVI, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.064 | 11/45 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.553×** | -5.8 | 4e-06 | 23/44 (AsPC-1, SW480, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.588×** | -5.1 | 1e-04 | 21/44 (KATO III, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.675×** | -4.0 | 0.012 | 15/46 (C32, HepG2/C3A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.679×** | -3.9 | 0.012 | 10/46 (AsPC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -3.8 | 0.017 | 17/46 (SNU-423, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.772×** | -3.7 | 0.019 | 16/48 (RKO, SW 1088, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.509×** | -3.6 | 0.027 | 11/38 (LOX-IMVI, H4, …) | top dose only | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | **0.701×** | -3.5 | 0.037 | 10/44 (A549, HepG2/C3A, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.793×** | -3.3 | 0.053 | 13/47 (KATO III, A549, …) | rises with dose | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.724×** | -3.3 | 0.054 | 11/47 (AsPC-1, C32, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.796×** | -3.3 | 0.054 | 13/48 (AsPC-1, SW 1088, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **0.733×** | -3.2 | 0.076 | 13/46 (BT-474, hTERT-HPNE, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.740×** | -3.1 | 0.097 | 12/48 (A498, LS 180, …) | all doses, flat |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.734×** | -3.0 | 0.097 | 12/44 (HepG2/C3A, A498, …) | top dose only |  |
| [[Trifluridine (drug)]] 0.5 µM |  | **0.743×** | -3.0 | 0.097 | 11/45 (HCT15, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.52 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0502× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 7.03 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.48× (z +9.7) | [[Ponatinib (drug)]] 5 µM 0.0359× (z -10.6) |
| [[HOP62 (line)]] | alt | 5.18 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +9.4) | [[Tadalafil (drug)]] 0.05 µM 0.0710× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 13.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 5.33 | 0 | 1 | — | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.0827× (z -9.8) |
| [[A-427 (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.113× (z -10.5) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A549 (line)]] | wt | 5.36 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0921× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 8.67 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.105× (z -10.3) |
| [[H4 (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0528× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +9.5) | — |
| [[LoVo (line)]] | wt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +11.5) | — |
| [[NCI-H460 (line)]] | wt | 4.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.29× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 5.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 6.64 | 0 | 1 | — | [[Hesperidin (drug)]] 0.5 µM 0.0753× (z -9.6) |
| [[SW48 (line)]] | wt | 11.2 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0690× (z -9.5) |
| [[SW480 (line)]] | alt | 8.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM41]] | +0.82 | +0.79 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[RFPL3S]] | +0.80 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.80 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[PILRA]] | +0.79 | +0.79 / +0.86 | both halves | 7e-06 |  |
| [[VWCE]] | +0.77 | +0.79 / +0.80 | both halves | 7e-06 |  |
| [[MYO15A]] | +0.77 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[CCNP]] | +0.76 | +0.70 / +0.84 | both halves | 7e-06 |  |
| [[ORAI2]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[PYGM]] | +0.76 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[HPX]] | +0.76 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[PHKG1]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R1B]] | -0.61 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[RPE]] | -0.61 | -0.66 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TINCR's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TINCR's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.805). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.9, -18.7); signed map (14.3, 12.8). **Vector** length 91.2, 18.2% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +16.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.2 | +1.5 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -5.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.4 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | TINCR ubiquitin domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,558,167-5,578,349 (-) |
| Ensembl biotype | protein_coding |
| Also known as | pTINCR, FLJ90734, NCRNA00036, LINC00036, onco-lncRNA-16, TUBL; previously PLAC2 |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A2R8Y7D0](https://www.uniprot.org/uniprotkb/A0A2R8Y7D0) (Ubiquitin domain-containing protein TINCR):

> Promotes epithelial differentiation by enhancing the sumoylation and activation of CDC42. Promotes keratinocyte proliferation. This contributes to the maintenance of skin homeostasis by enhancing wound healing after skin injury (By similarity). Acts as a tumor suppressor in epithelial tumors.

**Summary**, from NCBI Gene [257000](https://www.ncbi.nlm.nih.gov/gene/257000):

> This gene produces a spliced long non-coding RNA that binds RNAs. This transcript interacts with staufen-1 protein to regulate the stability of mRNAs for genes involved in the differentiation of epidermal tissue. Variation in this gene may be associated with cancer progression. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:14607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14607) · Entrez [257000](https://www.ncbi.nlm.nih.gov/gene/257000) · UniProt [A0A2R8Y7D0](https://www.uniprot.org/uniprotkb/A0A2R8Y7D0) · Ensembl [ENSG00000223573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223573)

## Data

Gene col 13350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13350); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13350]; `tensor/DDL_lfc|DDL_z.npy` [13350]; `embed/gene_vectors.npy` [13350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13350 or target_col == 13350). Every well: [[TINCR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TINCR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
