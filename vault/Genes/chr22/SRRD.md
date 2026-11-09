---
symbol: "SRRD"
type: "gene"
col: 1868
ensembl_id: "ENSG00000100104"
name: "SRR1 domain containing"
location: "22q12.1"
module: 16
arm: "+"
pooled_cpm: 6.57
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# SRRD

*SRR1 domain containing* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.64× (z +7.2, q 3e-10, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.657× (z -8.7, q 2e-15, down in 25 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS18A]] (+0.70, fdr 7e-06), [[MRFAP1]] (+0.70, fdr 7e-06), [[CIAO1]] (+0.69, fdr 7e-06); moves opposite to [[GNAS]] (-0.64, fdr 1e-05), [[KPNB1-DT]] (-0.60, fdr 2e-04), [[KDELR1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1868.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.64×** | +7.2 | 3e-10 | 28/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +7.0 | 9e-10 | 24/47 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +6.7 | 5e-09 | 19/48 (A-427, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +6.6 | 6e-09 | 14/39 (SW480, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.6 | 2e-06 | 4/48 (CFPAC-1, A549, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +5.5 | 3e-06 | 17/42 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.4 | 5e-06 | 15/40 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +5.4 | 5e-06 | 13/47 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.2 | 1e-05 | 11/46 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +4.8 | 1e-04 | 17/45 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.54×** | +4.5 | 3e-04 | 12/36 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.0 | 0.003 | 11/47 (SW1417, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.004 | 11/45 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **1.31×** | +3.8 | 0.007 | 11/34 (NCI-H460, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.007 | 12/45 (NCI-H23, A-172, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.016 | 4/33 (SK-MEL-2, A498, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.036 | 3/43 (MIA PaCa-2, CFPAC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.039 | 1/44 (MIA PaCa-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.27×** | +3.1 | 0.056 | 3/40 (SW48, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1868.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -8.7 | 2e-15 | 25/42 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.659×** | -5.9 | 1e-06 | 16/40 (LOX-IMVI, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -5.4 | 1e-05 | 16/41 (SK-MEL-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Silodosin (drug)]] 5 µM |  | **0.753×** | -4.0 | 0.009 | 10/43 (HepG2/C3A, HS-578T, …) | inconsistent across doses |  |
| [[Tazarotene (drug)]] 0.5 µM |  | 0.802× | -3.2 | 0.13 | 9/45 (AN3 CA, HepG2/C3A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1868. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.42 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0450× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[HEC-1-A (line)]] | alt | 8.52 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -11.2) |
| [[HOP62 (line)]] | alt | 4.91 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -9.9) |
| [[HS-578T (line)]] | alt | 8.73 | 0 | 1 | — | [[Sulfatinib (drug)]] 0.05 µM 0.100× (z -10.5) |
| [[LoVo (line)]] | wt | 7.13 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0820× (z -19.8) |
| [[PANC-1 (line)]] | alt | 5.57 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.77 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1868), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS18A]] | +0.70 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[MRFAP1]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[CIAO1]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[RTL6]] | +0.69 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[MANBAL]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[ZNF468]] | +0.68 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[DNAJC14]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[ZNF317]] | +0.67 | +0.60 / +0.80 | both halves | 7e-06 |  |
| [[DRG2]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[KLHL9]] | +0.65 | +0.47 / +0.74 | both halves | 2e-05 |  |
| [[TMEM185B]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.64 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[KPNB1-DT]] | -0.60 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[KDELR1]] | -0.59 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[EHBP1-AS1]] | -0.57 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[CCNO-DT]] | -0.56 | -0.31 / -0.60 | both halves | 2e-04 |  |
| [[EOGT-DT]] | -0.56 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[ABHD15-AS1]] | -0.56 | -0.26 / -0.57 | both halves | 4e-04 |  |
| [[OXR1-AS1]] | -0.55 | -0.24 / -0.53 | both halves | 5e-04 |  |
| [[ZNF451-AS1]] | -0.54 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[NFKBID]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[C12orf57]] | -0.53 | -0.20 / -0.63 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SRRD's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.0, -0.9); signed map (0.0, -29.1). **Vector** length 55.2, 7.27% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.4 | +6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.8 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.3 | +5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +3.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -8.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -5.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.2 | +0.9 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.1 | -2.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -0.9 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.8 | -0.0 |
|  | [[Rifaximin (drug)]] 5 µM |  | -0.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | SRR1 domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:26,483,877-26,494,658 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HC/HCC, SRR1L |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UH36](https://www.uniprot.org/uniprotkb/Q9UH36) (SRR1-like protein):

> Plays a role in the regulation of heme biosynthesis and in the regulation of the expression of core clock genes.

**Summary**, from NCBI Gene [402055](https://www.ncbi.nlm.nih.gov/gene/402055):

> Predicted to be involved in regulation of circadian rhythm and regulation of heme biosynthetic process. Predicted to be active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33910) · Entrez [402055](https://www.ncbi.nlm.nih.gov/gene/402055) · UniProt [Q9UH36](https://www.uniprot.org/uniprotkb/Q9UH36) · Ensembl [ENSG00000100104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100104)

## Data

Gene col 1868: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1868); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1868, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1868]; `tensor/DDL_lfc|DDL_z.npy` [1868]; `embed/gene_vectors.npy` [1868]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1868 or target_col == 1868). Every well: [[SRRD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRRD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
