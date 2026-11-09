---
symbol: "DPH2"
type: "gene"
col: 5368
ensembl_id: "ENSG00000132768"
name: "diphthamide biosynthesis 2"
location: "1p34.1"
module: 1
arm: "+"
pooled_cpm: 3.0
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# DPH2

*diphthamide biosynthesis 2* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.39× (z +8.8, q 6e-16, up in 4 of 12 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.59× (z +6.6, q 5e-09, up in 12 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.660× (z -6.0, q 9e-07, down in 18 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT61A]] (+0.76, fdr 7e-06), [[NOL6]] (+0.75, fdr 7e-06), [[METTL1]] (+0.72, fdr 7e-06); moves opposite to [[BEX3]] (-0.56, fdr 3e-05), [[KAT2B]] (-0.55, fdr 1e-05), [[MEGF9]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5368.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.39×** | +8.8 | 6e-16 | 4/12 (SW480, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.45×** | +8.7 | 7e-16 | 2/4 (PANC-1, J82) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +8.2 | 4e-14 | 7/14 (SHP-77, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.07×** | +7.3 | 3e-11 | 6/14 (A498, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +6.6 | 5e-09 | 12/44 (Panc 03.27, CFPAC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +6.6 | 5e-09 | 18/34 (NCI-H23, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.91×** | +6.0 | 1e-07 | 0/4 | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.9 | 3e-07 | 12/25 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.6 | 2e-06 | 11/33 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +4.9 | 5e-05 | 8/42 (NCI-H23, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.62×** | +4.9 | 6e-05 | 10/45 (A-172, SNU-423, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +4.6 | 2e-04 | 7/42 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.55×** | +4.4 | 5e-04 | 7/33 (C-33 A, A498, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +4.3 | 7e-04 | 11/43 (SW480, PANC-1, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.1 | 0.002 | 4/46 (PANC-1, RKO, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.49×** | +4.0 | 0.002 | 7/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.004 | 6/39 (MIA PaCa-2, HOP62, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.45×** | +3.7 | 0.006 | 9/32 (A498, PANC-1, …) | two highest doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.036 | 5/42 (J82, SW480, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.050 | 4/40 (PANC-1, A-172, …) | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.060 | 1/39 (SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5368.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.660×** | -6.0 | 9e-07 | 18/44 (KATO III, A498, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.666×** | -4.2 | 0.008 | 11/42 (RPMI-7951, A498, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.689×** | -3.7 | 0.043 | 17/37 (SHP-77, Panc 03.27, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.713×** | -3.5 | 0.070 | 8/44 (SW480, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cyclosporin A (drug)]] 5 µM |  | 0.745× | -3.0 | 0.27 | 6/44 (SK-MEL-2, HCT15, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 3.50 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.74× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.933 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT61A]] | +0.76 | +0.79 / +0.72 | both halves | 7e-06 | STRING 424 |
| [[NOL6]] | +0.75 | +0.76 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[METTL1]] | +0.72 | +0.76 / +0.67 | both halves | 7e-06 | STRING 547 |
| [[IMP4]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[WDR46]] | +0.71 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[NOC4L]] | +0.70 | +0.73 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TBL3]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[PUS1]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 | STRING 618 |
| [[NIP7]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[GEMIN4]] | +0.67 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[IFRD2]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TWNK]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEX3]] | -0.56 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[KAT2B]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[MEGF9]] | -0.54 | -0.55 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DPH2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DPH2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.6, -34.3); signed map (-3.5, -44.4). **Vector** length 51.0, 6.52% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.50 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.51 to 23); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.54 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.6 | +7.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.1 | +6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.0 | +4.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.0 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +6.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +4.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.9 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.8 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | diphthamide biosynthesis 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:43,970,000-43,973,369 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DPH2L2 |
| Gene groups (HGNC) | Diphthamide biosynthesis genes |
| Reactome | 2 pathways, smallest: Synthesis of diphthamide-EEF2; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQC3](https://www.uniprot.org/uniprotkb/Q9BQC3) (2-(3-amino-3-carboxypropyl)histidine synthase subunit 2):

> Required for the first step of diphthamide biosynthesis, a post-translational modification of histidine which occurs in elongation factor 2. DPH1 and DPH2 transfer a 3-amino-3-carboxypropyl (ACP) group from S-adenosyl-L-methionine (SAM) to a histidine residue, the reaction is assisted by a reduction system comprising DPH3 and a NADH-dependent reductase (By similarity). Facilitates the reduction of the catalytic iron-sulfur cluster found in the DPH1 subunit (By similarity).

**Summary**, from NCBI Gene [1802](https://www.ncbi.nlm.nih.gov/gene/1802):

> This gene is one of two human genes similar to the yeast gene dph2. The yeast gene was identified by its ability to complement a diphthamide mutant strain, and thus probably functions in diphthamide biosynthesis. Diphthamide is a post-translationally modified histidine residue present in elongation factor 2 (EF2) that is the target of diphtheria toxin ADP-ribosylation. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:3004](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3004) · Entrez [1802](https://www.ncbi.nlm.nih.gov/gene/1802) · UniProt [Q9BQC3](https://www.uniprot.org/uniprotkb/Q9BQC3) · Ensembl [ENSG00000132768](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132768)

## Data

Gene col 5368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5368); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5368]; `tensor/DDL_lfc|DDL_z.npy` [5368]; `embed/gene_vectors.npy` [5368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5368 or target_col == 5368). Every well: [[DPH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
