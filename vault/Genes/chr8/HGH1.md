---
symbol: "HGH1"
type: "gene"
col: 14003
ensembl_id: "ENSG00000235173"
name: "HGH1 cochaperone"
location: "8q24.3"
module: 1
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 49
n_dd_up: 31
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# HGH1

*HGH1 cochaperone* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.68× (z +16.8, q 0e+00, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +9.2, q 4e-18, up in 18 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.652× (z -4.0, q 0.023, down in 10 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMG1]] (+0.70, fdr 7e-06), [[BCS1L]] (+0.69, fdr 7e-06), [[IFRD2]] (+0.67, fdr 7e-06); moves opposite to [[MRPL33]] (-0.64, fdr 1e-05), [[SERF2]] (-0.64, fdr 1e-05), [[NDUFA4]] (-0.61, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.68×** | +16.8 | 0e+00 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.55×** | +13.9 | 2e-41 | 8/9 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.48×** | +10.6 | 7e-24 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **3.10×** | +10.4 | 4e-23 | 32/43 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +9.2 | 4e-18 | 18/26 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +8.4 | 3e-15 | 17/31 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.47×** | +8.3 | 9e-15 | 22/40 (KATO III, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.38×** | +7.9 | 1e-13 | 18/28 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.33×** | +7.7 | 7e-13 | 29/43 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.73×** | +7.1 | 8e-11 | 7/42 (NCI-H2347, NCI-H2030, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.18×** | +6.9 | 3e-10 | 16/38 (LS 180, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.03×** | +6.5 | 4e-09 | 9/38 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.02×** | +6.4 | 5e-09 | 13/40 (LoVo, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +5.8 | 2e-07 | 4/10 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.89×** | +5.6 | 8e-07 | 8/18 (Hs 766T, NCI-H1573, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.61×** | +4.2 | 7e-04 | 7/26 (PANC-1, A498, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.68×** | +3.4 | 0.018 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.023 | 1/41 (RPMI-7951) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Phenytoin (sodium) (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.024 | 0/39 | inconsistent across doses | position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.93×** | +3.2 | 0.034 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.40×** | +3.0 | 0.047 | 0/36 | inconsistent across doses | position effect removed |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.38×** | +2.9 | 0.069 | 3/40 (BT-474, SW480, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.25×** | +2.8 | 0.089 | 1/40 (NCI-H460) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14003.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.652×** | -4.0 | 0.023 | 10/34 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.654×** | -3.9 | 0.023 | 13/43 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.691× | -3.4 | 0.11 | 11/37 (NCI-H2030, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Altretamine (drug)]] 5 µM |  | 0.709× | -3.1 | 0.29 | 5/35 (BT-474, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.876 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.723 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.853 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.958 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.954 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.982 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMG1]] | +0.70 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[BCS1L]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[IFRD2]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 | same gene group |
| [[C7orf25]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[RRP9]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 | STRING 448 |
| [[ZNF252P-1]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[RRS1]] | +0.64 | +0.64 / +0.66 | both halves | 7e-06 | STRING 731 |
| [[RUVBL1]] | +0.63 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[UTP15]] | +0.62 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[PNPO]] | +0.62 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[CCDC86]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[WDR77]] | +0.62 | +0.63 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL33]] | -0.64 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[SERF2]] | -0.64 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[NDUFA4]] | -0.61 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[UQCRB]] ⚠ | -0.61 | -0.59 / -0.46 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TALAM1]] | -0.60 | -0.40 / -0.65 | both halves | 5e-05 |  |
| [[RPLP2]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[NDUFA1]] | -0.60 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[RPLP1]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[RPL37A]] ⚠ | -0.59 | -0.53 / -0.50 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6C]] | -0.58 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[COX6A1]] | -0.58 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[RPS19]] | -0.57 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[GABARAPL2]] | -0.57 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[SEZ6L2]] | -0.57 | -0.58 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HGH1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.5, -39.7); signed map (-3.3, -43.9). **Vector** length 43.9, 5.37% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +16.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.0 | +13.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.8 | +5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.7 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +7.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.5 | +3.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -1.9 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | +0.7 |
|  | [[Rifaximin (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | HGH1 cochaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,137,774-144,140,851 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40907, LOC51236, Brp16; previously C8orf30A, FAM203B, C8orf30B, FAM203A |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTY7](https://www.uniprot.org/uniprotkb/Q9BTY7) (Co-chaperone protein HGH1 homolog):

> Co-chaperone involved in the folding of nascent eukaryotic elongation factor eEF2, an essential component of the translation machinery. Recognizes a non-native conformation in the central domain of eEF2 and recruits the chaperonin-containing T-complex (TRiC) to the C-terminal region of the nascent polypeptide, preventing unproductive interactions and promoting efficient folding of the N-terminal GTPase domain. May also assist in eEF2 maturation by recruiting the molecular chaperone Hsp90.

**Summary**, from NCBI Gene [51236](https://www.ncbi.nlm.nih.gov/gene/51236):

> Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24161) · Entrez [51236](https://www.ncbi.nlm.nih.gov/gene/51236) · UniProt [Q9BTY7](https://www.uniprot.org/uniprotkb/Q9BTY7) · Ensembl [ENSG00000235173](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235173)

## Data

Gene col 14003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14003); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14003]; `tensor/DDL_lfc|DDL_z.npy` [14003]; `embed/gene_vectors.npy` [14003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14003 or target_col == 14003). Every well: [[HGH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HGH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
