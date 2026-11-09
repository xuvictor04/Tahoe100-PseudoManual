---
symbol: "BMS1P1"
type: "gene"
col: 12825
ensembl_id: "ENSG00000204177"
name: "BMS1 pseudogene 1"
location: "10q11.22"
module: 25
arm: "-"
pooled_cpm: 5.67
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# BMS1P1

*BMS1 pseudogene 1* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Sunitinib (drug)]] 5 µM: 1.49× (z +4.7, q 0.002, up in 11 of 41 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.43× (z +4.2, q 0.006, up in 10 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.628× (z -7.7, q 1e-11, down in 23 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMS1P1-1]] (+0.81, fdr 7e-06, ⚠ same locus), [[AGAP13P]] (+0.57, fdr 4e-05, ⚠ same locus), [[TAF3]] (+0.55, fdr 2e-05), [[MRPL32]] (+0.54, fdr 1e-04), [[KLHL20]] (+0.52, fdr 5e-05); moves opposite to [[HUWE1]] (-0.58, fdr 4e-05), [[ZNF664]] (-0.56, fdr 8e-05), [[DBN1]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12825.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.7 | 0.002 | 11/41 (HT-29, H4, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 0.006 | 10/44 (A498, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.48× | +3.3 | 0.15 | 4/35 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.32× | +3.3 | 0.15 | 3/44 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.31× | +3.2 | 0.16 | 3/44 (SW480, HT-29, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12825.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.628×** | -7.7 | 1e-11 | 23/38 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.535×** | -7.3 | 9e-11 | 27/45 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.587×** | -6.2 | 1e-07 | 24/45 (CFPAC-1, HS-578T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.626×** | -5.4 | 8e-06 | 17/43 (SW480, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.635×** | -5.3 | 1e-05 | 17/45 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.684×** | -4.2 | 0.002 | 16/34 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.695×** | -4.2 | 0.002 | 14/45 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.681×** | -4.2 | 0.002 | 16/42 (HT-29, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.707×** | -4.0 | 0.004 | 11/45 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.735×** | -3.6 | 0.020 | 13/40 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.751×** | -3.3 | 0.048 | 14/37 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.762×** | -3.1 | 0.076 | 11/43 (A549, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.597×** | -3.1 | 0.076 | 9/34 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.603×** | -3.1 | 0.084 | 10/42 (A549, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.05 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.7) |
| [[A549 (line)]] | wt | 9.02 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 3.85 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0791× (z -11.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.293× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 6.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -8.6) |
| [[COLO 205 (line)]] | alt | 8.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 6.15 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[HS-578T (line)]] | alt | 5.01 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0682× (z -9.9) |
| [[J82 (line)]] | alt | 2.40 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0884× (z -11.1) |
| [[KATO III (line)]] | alt | 4.88 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0950× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 5.97 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0487× (z -14.3) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 7.92 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0586× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.183× (z -8.6) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 5.15 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0892× (z -9.3) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 6.15 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0719× (z -9.2) |
| [[SW 900 (line)]] | alt | 5.71 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0831× (z -8.6) |
| [[A-172 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1P1-1]] | +0.81 | +0.80 / +0.76 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[AGAP13P]] | +0.57 | +0.70 / +0.41 | both halves | 4e-05 | ⚠ same locus (16.7 kb, same strand: neighbours can correlate without regulation) |
| [[TAF3]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[MRPL32]] | +0.54 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[KLHL20]] | +0.52 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[SNU13]] | +0.51 | +0.36 / +0.64 | both halves | 9e-05 |  |
| [[CDC37L1]] | +0.50 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[CHKB]] | +0.50 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[ZNF594-DT]] | +0.50 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[MTFMT]] | +0.50 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[NLRX1]] | +0.50 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[MALSU1]] | +0.50 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[SELENOH]] | +0.50 | +0.21 / +0.58 | both halves | 7e-04 |  |
| [[NCBP2AS2]] | +0.50 | +0.28 / +0.60 | both halves | 3e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HUWE1]] | -0.58 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[ZNF664]] | -0.56 | -0.37 / -0.63 | both halves | 8e-05 |  |
| [[DBN1]] | -0.54 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[HDLBP]] | -0.53 | -0.32 / -0.64 | both halves | 2e-04 |  |
| [[DYNC1H1]] | -0.52 | -0.31 / -0.63 | both halves | 2e-04 |  |
| [[EEF1A1]] | -0.51 | -0.35 / -0.63 | both halves | 1e-04 |  |
| [[G6PD]] | -0.50 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[NRAS]] | -0.50 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[CLTC]] | -0.50 | -0.29 / -0.61 | both halves | 2e-04 |  |
| [[CTNNA1]] | -0.49 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[FLNA]] | -0.49 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[IQGAP1]] | -0.49 | -0.33 / -0.60 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.379). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-34.0, -20.5); signed map (-10.4, -6.0). **Vector** length 52.3, 7.04% of its response variance represented; |z| ≥ 3 in 791 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.7 | +4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +0.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +2.2 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | -3.2 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | -0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.8 | +2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.5 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -5.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | BMS1 pseudogene 1 |
| Locus type | pseudogene |
| Location | 10q11.22 — chr10:46,788,397-46,799,819 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously BMS1LP1, BMS1P5, BMS1LP5 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23649) · Entrez [399761](https://www.ncbi.nlm.nih.gov/gene/399761) · Ensembl [ENSG00000204177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204177)

## Data

Gene col 12825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12825); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12825]; `tensor/DDL_lfc|DDL_z.npy` [12825]; `embed/gene_vectors.npy` [12825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12825 or target_col == 12825). Every well: [[BMS1P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMS1P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
