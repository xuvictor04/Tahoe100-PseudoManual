---
symbol: "CCNG1"
type: "gene"
col: 3451
ensembl_id: "ENSG00000113328"
name: "cyclin G1"
location: "5q34"
module: 45
arm: "+"
pooled_cpm: 66.18
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/045", "written"]
generated_by: "tahoemap"
---

# CCNG1

*cyclin G1* — 5q34

> [!summary] In one line
> CCNG1 encodes cyclin G1, an atypical cyclin that is one of p53's most reliably induced direct targets and that has been reported to feed back on p53 by recruiting PP2A to MDM2.

## What it is

Cyclin G1 carries a recognisable cyclin box but behaves very little like a cell-cycle cyclin. It has no established CDK partner that drives a cell-cycle transition, and it is not expressed with the periodicity that defines the canonical cyclins. What it does have is an unusually clean relationship to p53: cyclin G was identified as a transcriptional target of p53, and it is among the genes induced most consistently and most strongly when p53 is activated, across many cell types and many kinds of stress.

Its proposed function is as a phosphatase-targeting subunit. Cyclin G1 associates with the B′/B56 (PPP2R5) regulatory subunits of protein phosphatase 2A in a p53-dependent manner, and it also binds MDM2, where it markedly stimulates PP2A's ability to dephosphorylate MDM2 at T216 (and reduces phosphorylation at S166 of the human protein). Because dephosphorylated MDM2 binds p53 more avidly, the net effect is to lower p53. Cells lacking cyclin G have hyperphosphorylated MDM2 and higher p53 protein, which is the main genetic support for the model. The arrangement makes cyclin G1 a negative-feedback component: p53 induces it, and it damps p53 — the same topology as [[MDM2]], reached by a different mechanism. Beyond this, cyclin G1 has been implicated in hepatocyte proliferation and liver regeneration, and the gene is amplified or overexpressed in a subset of tumours.

## What is uncertain

The PP2A–MDM2 mechanism rests essentially on one 2002 study and the reviews that summarise it; I am not aware of a clear independent replication, and the model should be held more loosely than cyclin G1's status as a p53 target. Even within that work the dose–response is paradoxical: low re-expression of cyclin G increased p53-associated MDM2 while higher levels had the opposite effect, which is hard to reconcile with a simple linear brake. Whether cyclin G1 is a cyclin in the functional sense — a subunit that activates a CDK — remains unresolved. Reports also split on whether cyclin G1 is net growth-promoting or growth-suppressing, with the direction varying by cell type and p53 status. The summary position worth holding: that p53 induces CCNG1 is well established; what CCNG1 then does is not.

## References

- Okamoto & Beach, 1994, The EMBO Journal — showed cyclin G is a transcriptional target of p53.
- Okamoto et al., 1996, Molecular and Cellular Biology — reported a p53-dependent association between cyclin G and the B′ subunit of PP2A.
- Okamoto et al., 2002, Molecular Cell — cyclin G binds MDM2 and recruits PP2A to dephosphorylate it at T216; cyclin G null cells show hyperphosphorylated MDM2 and elevated p53.
- Fischer, 2017, Oncogene — census of p53 target genes, placing CCNG1 among the consistently induced direct targets.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.40× (z +6.0, q 1e-06, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.650× (z -10.8, q 1e-24, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM210B]] (+0.69, fdr 7e-06), [[HSDL2]] (+0.67, fdr 1e-05), [[PCYOX1]] (+0.65, fdr 7e-06); moves opposite to [[NOP56]] (-0.59, fdr 1e-05), [[ZNF75A]] (-0.52, fdr 3e-05), [[MYH3]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TP53INP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3451.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +6.0 | 1e-06 | 28/48 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 2e-06 | 29/48 (SW1417, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.25×** | +5.7 | 2e-06 | 24/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.32×** | +4.9 | 1e-04 | 24/47 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +4.7 | 2e-04 | 25/48 (HEC-1-A, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +4.2 | 0.002 | 21/47 (MIA PaCa-2, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.0 | 0.005 | 3/49 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.014 | 20/47 (LoVo, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +3.6 | 0.018 | 18/42 (SW480, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.22×** | +3.5 | 0.029 | 20/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.045 | 17/48 (SK-MEL-2, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.12 | 14/49 (C32, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3451.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.650×** | -10.8 | 1e-24 | 33/48 (A-427, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.620×** | -8.2 | 7e-14 | 40/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -7.9 | 6e-13 | 34/48 (HCT15, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -6.1 | 1e-07 | 36/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -5.6 | 2e-06 | 30/48 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.675×** | -5.2 | 2e-05 | 30/47 (SW480, KATO III, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | **0.808×** | -3.8 | 0.010 | 20/48 (AsPC-1, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.750×** | -3.7 | 0.018 | 20/48 (HT-29, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | **0.817×** | -3.6 | 0.018 | 19/47 (SNU-1, SW 900, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.680×** | -3.6 | 0.018 | 19/48 (SW480, SW 900, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -3.6 | 0.018 | 22/48 (Hs 766T, SW480, …) | top dose only |  |
| [[Bergenin (drug)]] 0.5 µM |  | **0.826×** | -3.4 | 0.031 | 19/48 (CHP-212, Panc 03.27, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | **0.830×** | -3.3 | 0.039 | 21/48 (LOX-IMVI, H4, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.703×** | -3.3 | 0.042 | 19/48 (HOP62, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.835× | -3.1 | 0.070 | 15/48 (LS 180, LoVo, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.784×** | -3.1 | 0.070 | 18/48 (PANC-1, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.787×** | -3.0 | 0.072 | 17/48 (HT-29, NCI-H1792, …) | rises with dose | low cells (technical?); noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3451. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 94.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -12.4) |
| [[HCT15 (line)]] | alt | 59.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -15.0) |
| [[LS 180 (line)]] | wt | 97.7 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 2.57× (z +10.2) ⚠ cell-cycle shift, explains ~21% of this change | [[Harringtonine (drug)]] 5 µM 0.415× (z -9.2) |
| [[SNU-1 (line)]] | wt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 68.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.585× (z -9.7) |
| [[A-427 (line)]] | wt | 80.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -20.8) |
| [[CHP-212 (line)]] | wt | 86.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -10.0) |
| [[H4 (line)]] | wt | 65.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.5) |
| [[HOP62 (line)]] | alt | 49.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -10.9) |
| [[Hs 766T (line)]] | wt | 65.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -9.3) |
| [[HT-29 (line)]] | alt | 64.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.398× (z -10.2) |
| [[LoVo (line)]] | wt | 165 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.400× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 28.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 74.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.462× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 88.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -10.2) |
| [[NCI-H661 (line)]] | alt | 39.9 | 0 | 1 | — | [[Tomivosertib (drug)]] 0.05 µM 0.0584× (z -9.5) |
| [[PANC-1 (line)]] | alt | 65.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.487× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 50.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.321× (z -9.4) |
| [[SNU-423 (line)]] | alt | 78.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -8.8) |
| [[SW 900 (line)]] | alt | 96.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.9) |
| [[A-172 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 94.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 88.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3451), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM210B]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[HSDL2]] | +0.67 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[PCYOX1]] | +0.65 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TMED4]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ATP6AP2]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[DNASE2]] | +0.60 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[LAMP2]] | +0.58 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[PLA2G12A]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[LTA4H]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[GM2A]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[CMBL]] | +0.56 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[CREG1]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP56]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[ZNF75A]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MYH3]] | -0.52 | -0.58 / -0.43 | both halves | 3e-05 |  |
| [[SURF6]] | -0.52 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[AFG3L1P]] | -0.52 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[UTP3]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[EIF3J]] | -0.51 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[FJX1]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[RBM26-AS1]] | -0.50 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[CLCF1]] | -0.50 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[BRIX1]] | -0.50 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[ZNF562]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53INP1]] | B | TP53INP1 activity raises CCNG1's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without TP53INP1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[TP53]] | B | TP53 activity weakens CCNG1's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 1.16× as strongly (z diff -0.76); rises at some drug-doses, falls at others (38% from rises): Homoharringtonine 0.05 µM: 0.66x vs 0.96x (z diff -3.9); Harringtonine 0.05 µM: 0.62x vs 0.83x (z diff -2.5); Belinostat 5 µM: 1.49x vs 1.11x (z diff -2.5) | 0.057 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; rises at some drug-doses, falls at others; the reference differs; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers CCNG1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[APOBEC3C]] | B | APOBEC3C activity raises CCNG1's level | lines that do not express APOBEC3C (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without APOBEC3C | 0.097 | ⚠ within organs, on part of the lines; also absent: MIR181A2HG, CRTAP |
| [[CRTAP]] | C | CRTAP activity raises CCNG1's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without CRTAP | 0.043 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.488). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-19.3, -18.8); signed map (-51.4, -7.4). **Vector** length 128, 35.5% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +6.3 | +5.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.9 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +6.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.0 | +2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.0 | +1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.8 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.7 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.3 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -5.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | cyclin G1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q34 — chr5:163,437,569-163,446,151 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CCNG |
| Gene groups (HGNC) | Cyclins |
| Hallmark sets | P53_PATHWAY, MTORC1_SIGNALING |
| Reactome | 4 pathways, smallest: Regulation of TP53 Degradation; Regulation of TP53 Expression and Degradation; Regulation of TP53 Activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P51959](https://www.uniprot.org/uniprotkb/P51959) (Cyclin-G1):

> May play a role in growth regulation. Is associated with G2/M phase arrest in response to DNA damage. May be an intermediate by which p53 mediates its role as an inhibitor of cellular proliferation (By similarity).

**Summary**, from NCBI Gene [900](https://www.ncbi.nlm.nih.gov/gene/900):

> The eukaryotic cell cycle is governed by cyclin-dependent protein kinases (CDKs) whose activities are regulated by cyclins and CDK inhibitors. The protein encoded by this gene is a member of the cyclin family and contains the cyclin box. The encoded protein lacks the protein destabilizing (PEST) sequence that is present in other family members. Transcriptional activation of this gene can be induced by tumor protein p53. Two transcript variants encoding the same protein have been identified for …

**Accessions** — [HGNC:1592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1592) · Entrez [900](https://www.ncbi.nlm.nih.gov/gene/900) · UniProt [P51959](https://www.uniprot.org/uniprotkb/P51959) · Ensembl [ENSG00000113328](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113328)

## Data

Gene col 3451: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3451); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3451, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3451]; `tensor/DDL_lfc|DDL_z.npy` [3451]; `embed/gene_vectors.npy` [3451]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3451 or target_col == 3451). Every well: [[CCNG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/CCNG1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
