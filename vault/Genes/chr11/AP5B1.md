---
symbol: "AP5B1"
type: "gene"
col: 14875
ensembl_id: "ENSG00000254470"
name: "adaptor related protein complex 5 subunit beta 1"
location: "11q13.1"
module: 65
arm: "-"
pooled_cpm: 8.7
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# AP5B1

*adaptor related protein complex 5 subunit beta 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.71× (z +6.4, q 1e-07, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.434× (z -5.2, q 7e-05, down in 18 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35F6]] (+0.65, fdr 7e-06), [[ZSCAN29]] (+0.64, fdr 1e-05), [[TOR1A]] (+0.63, fdr 2e-05); moves opposite to [[NKTR]] (-0.60, fdr 1e-05), [[IFT172]] (-0.59, fdr 3e-05), [[ARL3]] (-0.59, fdr 2e-05).
> It sits in the **-** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14875.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +6.4 | 1e-07 | 26/47 (LoVo, HOP62, …) | top dose only | position effect removed |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.38×** | +3.8 | 0.026 | 8/47 (NCI-H23, LOX-IMVI, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.026 | 11/47 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.026 | 11/42 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +3.7 | 0.026 | 7/25 (J82, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +3.6 | 0.026 | 12/38 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.5 | 0.032 | 14/46 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.4 | 0.044 | 11/47 (Hs 766T, HEC-1-A, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.049 | 10/46 (SNU-423, NCI-H1573, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.065 | 9/48 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +3.2 | 0.069 | 7/46 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.069 | 3/45 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.069 | 8/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.069 | 5/46 (PANC-1, LoVo, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.071 | 4/48 (Panc 03.27, J82, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.071 | 7/47 (NCI-H2030, NCI-H1573, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14875.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **0.434×** | -5.2 | 7e-05 | 18/40 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.649×** | -5.2 | 7e-05 | 18/47 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.653×** | -5.1 | 7e-05 | 18/47 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.698×** | -4.3 | 0.003 | 17/44 (RKO, NCI-H1573, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.706×** | -4.1 | 0.004 | 19/47 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -3.9 | 0.009 | 9/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.762× | -3.1 | 0.14 | 10/45 (SW1417, HCT15, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.737× | -3.1 | 0.14 | 4/47 (BT-474, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 7.67 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.173× (z -8.5) |
| [[HOP62 (line)]] | alt | 5.76 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0561× (z -12.2) |
| [[Hs 766T (line)]] | wt | 4.97 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM 0.0724× (z -9.4) |
| [[J82 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.129× (z -10.7) |
| [[SHP-77 (line)]] | alt | 7.79 | 0 | 1 | — | [[AZD1390 (drug)]] 0.05 µM 0.111× (z -8.8) |
| [[A-172 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35F6]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ZSCAN29]] | +0.64 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TOR1A]] | +0.63 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ASXL2]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZNF629]] | +0.63 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ANKLE2]] | +0.61 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CENPBD1P]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ENOX2]] | +0.61 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[C7orf25]] | +0.59 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[PHF23]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[DNAJB12]] | +0.58 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CD2BP2]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKTR]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[IFT172]] | -0.59 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[ARL3]] | -0.59 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[EFHC1]] | -0.59 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[ORC4]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[COG6]] | -0.58 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[SEC22A]] | -0.58 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[ANAPC5]] | -0.58 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[AFMID]] | -0.57 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[ANKRD37]] | -0.57 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ELP2]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[TTC3]] | -0.56 | -0.52 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises AP5B1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CA9]] | B | CA9 activity lowers AP5B1's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.35× higher at baseline in the lines without CA9 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **-** arm (projection on the module's main direction -0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-9.3, 8.2); signed map (19.2, -28.7). **Vector** length 73.3, 12.0% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.3 | +6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.9 | +3.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.8 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[NG25 (drug)]] 5 µM |  | -2.4 | -5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.3 | -5.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 5 subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,773,898-65,780,976 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP1030, AP-5, DKFZp761E198 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Adaptor related protein complex 5 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2VPB7](https://www.uniprot.org/uniprotkb/Q2VPB7) (AP-5 complex subunit beta-1):

> As part of AP-5, a probable fifth adaptor protein complex it may be involved in endosomal transport.

**Summary**, from NCBI Gene [91056](https://www.ncbi.nlm.nih.gov/gene/91056):

> Involved in endosomal transport. Located in lysosomal membrane. Part of AP-type membrane coat adaptor complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25104) · Entrez [91056](https://www.ncbi.nlm.nih.gov/gene/91056) · UniProt [Q2VPB7](https://www.uniprot.org/uniprotkb/Q2VPB7) · Ensembl [ENSG00000254470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254470)

## Data

Gene col 14875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14875); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14875]; `tensor/DDL_lfc|DDL_z.npy` [14875]; `embed/gene_vectors.npy` [14875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14875 or target_col == 14875). Every well: [[AP5B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP5B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
