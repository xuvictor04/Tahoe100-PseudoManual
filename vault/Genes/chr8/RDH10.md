---
symbol: "RDH10"
type: "gene"
col: 4246
ensembl_id: "ENSG00000121039"
name: "retinol dehydrogenase 10"
location: "8q21.11"
module: 19
arm: "+"
pooled_cpm: 25.43
n_lines_expressing: 41
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 7
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# RDH10

*retinol dehydrogenase 10* — 8q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.24× (z +14.3, q 1e-43, up in 20 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Radotinib (drug)]] 5 µM: 0.775× (z -4.5, q 0.002, down in 15 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMDN2-AS1]] (+0.57, fdr 2e-05), [[ANXA10]] (+0.56, fdr 2e-05), [[SMOC1]] (+0.55, fdr 1e-05); moves opposite to [[ESD]] (-0.49, fdr 4e-05), [[MMS19]] (-0.47, fdr 4e-05), [[HDHD5]] (-0.46, fdr 3e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[RBM47]] → it (grade B ⚠); 7 go from it, the strongest it → [[NR4A2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.24×** | +14.3 | 1e-43 | 20/36 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +11.4 | 1e-27 | 20/37 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +8.4 | 7e-15 | 14/24 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +7.5 | 1e-11 | 20/37 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +6.8 | 1e-09 | 11/26 (J82, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +6.6 | 4e-09 | 16/31 (J82, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.2 | 6e-08 | 16/39 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.62×** | +5.2 | 1e-05 | 15/38 (RKO, LS 180, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +5.0 | 3e-05 | 11/38 (J82, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.003 | 11/37 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.40×** | +4.0 | 0.003 | 11/36 (LoVo, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.36×** | +3.8 | 0.006 | 15/38 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.016 | 11/37 (HEC-1-A, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.027 | 11/38 (A549, A498, …) | inconsistent across doses |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.046 | 6/38 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.093 | 12/37 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4246.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | **0.775×** | -4.5 | 0.002 | 15/39 (HT-29, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.703×** | -4.5 | 0.002 | 20/37 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.793×** | -4.2 | 0.006 | 18/40 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.739×** | -3.8 | 0.019 | 11/37 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.752×** | -3.6 | 0.037 | 16/36 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.759×** | -3.4 | 0.074 | 8/38 (AsPC-1, KATO III, …) | top dose only | plate-row cell shift; position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | 0.776× | -3.2 | 0.11 | 13/38 (SW 900, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | 0.623× | -3.1 | 0.12 | 9/35 (SW 900, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.774× | -3.1 | 0.12 | 10/37 (SW 900, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 116 | 0 | 18 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.117× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.118× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 79.9 | 0 | 11 (1 ⚠) | — | [[Budesonide (drug)]] 0.05 µM 0.139× (z -10.5) |
| [[COLO 205 (line)]] | alt | 142 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 8.33 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.88× (z +15.7) | — |
| [[A498 (line)]] | wt | 114 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 9.97 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +12.2) | [[Selinexor (drug)]] 5 µM 0.235× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 6.38 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.79× (z +10.5) | [[Proglumide (drug)]] 5 µM 0.0448× (z -10.0) |
| [[LoVo (line)]] | wt | 18.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +12.8) | — |
| [[NCI-H460 (line)]] | wt | 24.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0393× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.252× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 23.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 38.3 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.285× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.102× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +10.0) | — |
| [[RKO (line)]] | wt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 42.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -10.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.66 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.25 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMDN2-AS1]] | +0.57 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ANXA10]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[SMOC1]] | +0.55 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ARHGAP42]] | +0.55 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[CYP1B1]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 | STRING 476 |
| [[HIVEP2-DT]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[STEAP1B-AS1]] | +0.51 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[TTC6]] | +0.51 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[ADGRF5]] | +0.50 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[ETV6]] | +0.50 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[SLC12A2]] | +0.50 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[NOVA1]] | +0.50 | +0.52 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESD]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[MMS19]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[HDHD5]] | -0.46 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[TRIT1]] | -0.46 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[HEATR6]] | -0.46 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[LRRC40]] | -0.45 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[THOC1]] | -0.44 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD36B]] | -0.44 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[ALG9]] | -0.44 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[TAMM41]] | -0.44 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[YEATS2]] | -0.43 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[FKBP15]] | -0.43 | -0.37 / -0.41 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM47]] | B | RBM47 activity raises RDH10's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.70× lower at baseline in the lines without RBM47 | 0.008 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[PELI2]] | B | PELI2 activity raises RDH10's level | lines that do not express PELI2 (16) vs lines expressing it (34) | 1.69× lower at baseline in the lines without PELI2 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC02284, DNAJC12, ADAM28 |
| [[NTN4]] | B | NTN4 activity raises RDH10's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.85× lower at baseline in the lines without NTN4 | 0.033 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[CLDN10-AS1]] | B | CLDN10-AS1 activity raises RDH10's level | lines that do not express CLDN10-AS1 (31) vs lines expressing it (19) | 2.04× lower at baseline in the lines without CLDN10-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ADGRD1, AMBP, NPSR1-AS1 |
| [[BMP2]] | B | BMP2 activity raises RDH10's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.09× lower at baseline in the lines without BMP2 | 0.058 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[AADAC]] | B | AADAC activity raises RDH10's level | lines that do not express AADAC (34) vs lines expressing it (16) | 1.80× lower at baseline in the lines without AADAC | 0.079 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[LINC02284]] | B | LINC02284 activity raises RDH10's level | lines that do not express LINC02284 (17) vs lines expressing it (33) | 1.68× lower at baseline in the lines without LINC02284 | 0.093 | ⚠ within organs, on part of the lines; also absent: PELI2, CFH, ADAM28; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR4A2]] | B | RDH10 activity raises NR4A2's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 1.93× lower at baseline in the lines without RDH10 | 0.034 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |
| [[PELI2]] | B | RDH10 activity raises PELI2's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 1.95× lower at baseline in the lines without RDH10 | 0.043 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |
| [[BMP2]] | B | RDH10 activity raises BMP2's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 2.67× lower at baseline in the lines without RDH10 | 0.046 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |
| [[AHR]] | B | RDH10 activity raises AHR's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 1.88× lower at baseline in the lines without RDH10 | 0.068 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |
| [[MMS19]] | B | RDH10 activity lowers MMS19's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 1.30× higher at baseline in the lines without RDH10 | 0.074 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |
| [[NTN4]] | B | RDH10 activity raises NTN4's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 3.30× lower at baseline in the lines without RDH10 | 0.097 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |
| [[YEATS2]] | B | RDH10 activity lowers YEATS2's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 1.52× higher at baseline in the lines without RDH10 | 0.0999 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.347). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.9, 23.4); signed map (20.4, 54.5). **Vector** length 106, 26.2% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +14.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +6.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +2.6 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | +2.1 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.1 | +1.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | +1.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -3.8 | -2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -4.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.2 | -3.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | retinol dehydrogenase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.11 — chr8:73,294,602-73,325,281 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDR16C4 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 6 pathways, smallest: The canonical retinoid cycle in rods (twilight vision); RA biosynthesis pathway; Signaling by Retinoic Acid |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZV5](https://www.uniprot.org/uniprotkb/Q8IZV5) (Retinol dehydrogenase 10):

> Retinol dehydrogenase with a clear preference for NADP. Converts all-trans-retinol to all-trans-retinal. Has no detectable activity towards 11-cis-retinol, 9-cis-retinol and 13-cis-retinol.

**Summary**, from NCBI Gene [157506](https://www.ncbi.nlm.nih.gov/gene/157506):

> This gene encodes a retinol dehydrogenase, which converts all-trans-retinol to all-trans-retinal, with preference for NADP as a cofactor. Studies in mice suggest that this protein is essential for synthesis of embryonic retinoic acid and is required for limb, craniofacial, and organ development. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:19975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19975) · Entrez [157506](https://www.ncbi.nlm.nih.gov/gene/157506) · UniProt [Q8IZV5](https://www.uniprot.org/uniprotkb/Q8IZV5) · Ensembl [ENSG00000121039](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121039)

## Data

Gene col 4246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4246); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4246]; `tensor/DDL_lfc|DDL_z.npy` [4246]; `embed/gene_vectors.npy` [4246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4246 or target_col == 4246). Every well: [[RDH10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RDH10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
