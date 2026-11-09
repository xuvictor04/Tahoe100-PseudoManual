---
symbol: "RAB4A-AS1"
type: "gene"
col: 10865
ensembl_id: "ENSG00000177788"
name: "RAB4A antisense RNA 1"
location: "1q42.13"
module: 4
arm: "+"
pooled_cpm: 3.27
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# RAB4A-AS1

*RAB4A antisense RNA 1* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.39× (z +11.6, q 1e-28, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.01× (z +6.9, q 5e-10, up in 21 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.488× (z -7.1, q 7e-10, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GALT9]] (+0.70, fdr 7e-06), [[CCT2]] (+0.66, fdr 1e-05), [[TMEM185B]] (+0.66, fdr 7e-06); moves opposite to [[SELENOK]] (-0.65, fdr 1e-05), [[INAFM1]] (-0.60, fdr 1e-05), [[PMM1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.39×** | +11.6 | 1e-28 | 3/3 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +10.0 | 4e-21 | 11/15 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +7.6 | 5e-12 | 2/5 (NCI-H2347, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.64×** | +7.0 | 5e-10 | 13/43 (A-172, A498, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +6.9 | 5e-10 | 21/38 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +4.5 | 8e-04 | 16/45 (SW 900, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +4.3 | 0.002 | 10/42 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +3.8 | 0.009 | 5/41 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.018 | 5/44 (AsPC-1, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.032 | 8/44 (MIA PaCa-2, HS-578T, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.034 | 8/34 (LoVo, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.42×** | +3.3 | 0.039 | 4/14 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.089 | 3/38 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.39×** | +3.1 | 0.089 | 4/41 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.0 | 0.097 | 2/17 (SW480, SK-MEL-2) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10865.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.488×** | -7.1 | 7e-10 | 23/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.503×** | -6.8 | 3e-09 | 20/40 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.516×** | -6.6 | 1e-08 | 20/41 (SK-MEL-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.589×** | -5.2 | 2e-05 | 17/25 (SW1417, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.694×** | -5.1 | 4e-05 | 18/32 (NCI-H460, PANC-1, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.634×** | -4.3 | 0.001 | 18/42 (SK-MEL-2, PANC-1, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.655×** | -4.2 | 0.002 | 13/45 (NCI-H2030, AN3 CA, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.664×** | -4.1 | 0.004 | 17/42 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.698×** | -3.6 | 0.023 | 11/42 (SK-MEL-2, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.44 | 0 | 3 | — | [[Cobimetinib (drug)]] 5 µM 0.0550× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 6.90 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0497× (z -10.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.103× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 5.48 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -10.8) ⚠ cell-cycle shift, explains ~69% of this change |
| [[PANC-1 (line)]] | alt | 4.82 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -10.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[LS 180 (line)]] | wt | 3.43 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0707× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 2.51 | 0 | 1 | — | [[Darolutamide (drug)]] 0.5 µM 0.0628× (z -8.5) |
| [[SW480 (line)]] | alt | 2.93 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0924× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.968 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GALT9]] | +0.70 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[CCT2]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[TMEM185B]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[DHX15]] | +0.65 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[ATIC]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ZP3]] | +0.61 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ZNF239]] | +0.61 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[VMA21]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[EIF4G1]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MAT2A]] | +0.61 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[XK]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[NAA15]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOK]] | -0.65 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.60 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[PMM1]] | -0.60 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[ING2]] | -0.59 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.59 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[COG7]] | -0.59 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[ZMYM5]] | -0.58 | -0.32 / -0.65 | both halves | 2e-04 |  |
| [[NKAP]] | -0.58 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[AAMDC]] | -0.57 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[ARID4A]] | -0.57 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[GOLGA2]] | -0.57 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[TULP3]] | -0.57 | -0.62 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.637). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.6, -33.7); signed map (-8.5, -44.1). **Vector** length 53.3, 7.09% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.6 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +10.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.4 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.3 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -2.3 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.7 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.9 | -0.8 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | RAB4A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q42.13 — chr1:229,256,892-229,271,242 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55934](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55934) · Entrez [105373159](https://www.ncbi.nlm.nih.gov/gene/105373159) · Ensembl [ENSG00000177788](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177788)

## Data

Gene col 10865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10865); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10865]; `tensor/DDL_lfc|DDL_z.npy` [10865]; `embed/gene_vectors.npy` [10865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10865 or target_col == 10865). Every well: [[RAB4A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAB4A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
