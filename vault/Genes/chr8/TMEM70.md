---
symbol: "TMEM70"
type: "gene"
col: 10632
ensembl_id: "ENSG00000175606"
name: "transmembrane protein 70"
location: "8q21.11"
module: 11
arm: "+"
pooled_cpm: 11.94
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TMEM70

*transmembrane protein 70* — 8q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +10.1, q 3e-21, up in 34 of 45 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 2.68× (z +9.0, q 6e-17, up in 40 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.106×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP25L]] (+0.73, fdr 7e-06), [[NSUN5]] (+0.72, fdr 7e-06), [[ZNF593]] (+0.72, fdr 7e-06); moves opposite to [[FKBP9]] (-0.65, fdr 9e-06), [[NUCB1]] (-0.63, fdr 1e-05), [[TMEM30A]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10632.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.13×** | +10.1 | 3e-21 | 34/45 (COLO 205, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.68×** | +9.0 | 6e-17 | 40/46 (COLO 205, C32, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.31×** | +7.9 | 5e-13 | 36/43 (SW 900, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.23×** | +7.6 | 4e-12 | 41/46 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +7.3 | 3e-11 | 31/40 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.88×** | +6.0 | 2e-07 | 30/47 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.81×** | +5.6 | 1e-06 | 31/47 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.71×** | +5.1 | 3e-05 | 31/47 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.70×** | +5.0 | 3e-05 | 26/46 (COLO 205, A549, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.60×** | +4.5 | 5e-04 | 21/41 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.2 | 0.002 | 25/47 (HOP62, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +4.0 | 0.003 | 21/43 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.005 | 15/48 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +3.8 | 0.006 | 22/47 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +3.5 | 0.020 | 14/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.85×** | +3.3 | 0.030 | 8/44 (HOP62, HEC-1-A, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.81×** | +3.2 | 0.040 | 14/41 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.80×** | +3.1 | 0.043 | 8/44 (SW480, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (Hs 766T 0.106×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 19.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +13.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 8.71× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 19.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +14.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 9.85× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 14.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +11.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.42× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 9.93 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.106× (z -9.6) |
| [[KATO III (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 18.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +10.4) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[RKO (line)]] | wt | 31.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +11.0) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP25L]] | +0.73 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[NSUN5]] | +0.72 | +0.61 / +0.82 | both halves | 7e-06 |  |
| [[ZNF593]] | +0.72 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[EID2]] | +0.72 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[MRPL46]] | +0.72 | +0.57 / +0.79 | both halves | 9e-06 |  |
| [[MRPS18B]] | +0.71 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.71 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[PIGBOS1]] | +0.71 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[NT5C]] | +0.70 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[GSPT2]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[PHAX]] | +0.70 | +0.58 / +0.76 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.69 | +0.67 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP9]] | -0.65 | -0.57 / -0.68 | both halves | 9e-06 |  |
| [[NUCB1]] | -0.63 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.63 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[DHFR]] | -0.62 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[CRTAP]] | -0.61 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[FAM91A1]] | -0.61 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.61 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[TECR]] | -0.60 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.60 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[TMBIM6]] | -0.59 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[ERMP1]] | -0.59 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[RPN1]] | -0.58 | -0.49 / -0.67 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.756). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.2, 1.8); signed map (-3.0, -19.5). **Vector** length 62.1, 12.5% of its response variance represented; |z| ≥ 3 in 636 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.7 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.3 | +3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.0 | +3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +2.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.1 | -2.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -2.8 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 70 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.11 — chr8:73,972,437-73,982,783 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MC5DN2, FLJ20533 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUB7](https://www.uniprot.org/uniprotkb/Q9BUB7) (Transmembrane protein 70, mitochondrial):

> Scaffold protein that participates in the c-ring assembly of mitochondrial ATP synthase (F(1)F(0) ATP synthase or complex V) by facilitating the membrane insertion and oligomer formation of the subunit c/ATP5MC1 through its interaction. Therefore, participates in the early stage of mitochondrial ATP synthase biogenesis and also protects subunit c/ATP5MC1 against intramitochondrial proteolysis. In addition, binds the mitochondrial proton-transporting ATP synthase complexes I and may play a role …

**Summary**, from NCBI Gene [54968](https://www.ncbi.nlm.nih.gov/gene/54968):

> This gene likely encodes a mitochondrial membrane protein. The encoded protein may play a role in biogenesis of mitochondrial ATP synthase. Mutations in this gene have been associated with neonatal mitochondrial encephalocardiomyopathy due to ATP synthase deficiency. Alternatively spliced transcript variants have been described. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:26050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26050) · Entrez [54968](https://www.ncbi.nlm.nih.gov/gene/54968) · UniProt [Q9BUB7](https://www.uniprot.org/uniprotkb/Q9BUB7) · Ensembl [ENSG00000175606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175606)

## Data

Gene col 10632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10632); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10632]; `tensor/DDL_lfc|DDL_z.npy` [10632]; `embed/gene_vectors.npy` [10632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10632 or target_col == 10632). Every well: [[TMEM70 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM70.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
