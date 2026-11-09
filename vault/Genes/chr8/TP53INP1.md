---
symbol: "TP53INP1"
type: "gene"
col: 9037
ensembl_id: "ENSG00000164938"
name: "tumor protein p53 inducible nuclear protein 1"
location: "8q22.1"
module: 62
arm: "+"
pooled_cpm: 10.18
n_lines_expressing: 43
n_dd_up: 41
n_dd_down: 13
n_dd_up_clean: 34
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# TP53INP1

*tumor protein p53 inducible nuclear protein 1* — 8q22.1

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> TP53INP1 encodes a p53-induced nuclear protein that feeds back on p53 itself, helping license the apoptotic arm of the response while also restraining reactive oxygen and promoting autophagy.

## What it is

TP53INP1 (also p53DINP1, SIP, TEAP) is a small nuclear protein with no enzymatic domain, expressed as two splice isoforms. It was found as a p53-inducible gene whose own product alters p53-dependent apoptosis — that is, as a feedback component rather than a terminal effector. The mechanism reported for it is partnership with the kinase HIPK2: in complex with HIPK2, TP53INP1 promotes phosphorylation of p53 at Ser46, the modification most associated with shifting p53's output away from arrest and toward apoptosis. On that account, TP53INP1 is part of how an activated p53 biases its own program.

Two further activities complicate the simple pro-death picture. TP53INP1 is a substantial mediator of p53's antioxidant function, lowering intracellular reactive oxygen species — the opposite polarity to the redox arm represented by [[TP53I3]], and a reminder that p53 both raises and suppresses oxidative stress depending on the level of activation. It also carries an LC3-interacting region through which it binds LC3 and other ATG8-family proteins, driving autophagy and an autophagy-dependent form of cell death; so the "apoptosis" label attached to it in effector catalogues is narrower than the biology. In vivo, mice lacking Tp53inp1 show exacerbated colitis and colitis-associated cancer, which supports a genuine tumour-suppressive role, and the gene is responsive to p73 as well as p53.

## What is uncertain

The HIPK2/Ser46 mechanism rests on a small body of work, much of it using overexpressed protein, and how much of p53's Ser46 phosphorylation in an ordinary drug response depends on TP53INP1 is not established. The antioxidant and pro-autophagic-death roles are in tension: suppressing reactive oxygen is cytoprotective, promoting autophagic death is not, and which dominates appears to depend on the degree and duration of p53 activation in ways that have not been mapped. Whether its contribution to killing is apoptotic, autophagic, or both in different proportions by cell type remains open, so the effector annotation should be read as a label of convenience. Finally, because the transcript is not abundant, single-cell estimates for it are noisier than the headline program rank might suggest.

## References

- Okamura et al., 2001, Molecular Cell — identified p53DINP1/TP53INP1 as a p53-inducible gene regulating p53-dependent apoptosis.
- Tomasini et al., 2003, Journal of Biological Chemistry — showed TP53INP1 and HIPK2 act as partners in regulating p53 activity.
- Gommeaux et al., 2007, Molecular and Cellular Biology — colitis and colitis-associated cancer are exacerbated in TP53INP1-deficient mice.
- Cano et al., 2009, Cancer Research — TP53INP1 is a major mediator of p53's antioxidant function.
- Seillier et al., 2012, Cell Death and Differentiation — TP53INP1 binds LC3 and ATG8-family proteins through an LIR motif and promotes autophagy-dependent cell death.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.87× (z +9.2, q 3e-17, up in 29 of 40 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.05 µM: 1.58× (z +6.4, q 4e-08, up in 23 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.323× (z -11.8, q 3e-29, down in 34 of 40 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.348× (z -5.8, q 2e-06, down in 21 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FDXR]] (+0.73, fdr 7e-06), [[RPS27L]] (+0.72, fdr 7e-06), [[PHLDA3]] (+0.71, fdr 8e-06); moves opposite to [[EHBP1]] (-0.50, fdr 2e-05), [[HMBS]] (-0.49, fdr 4e-05), [[SERBP1]] (-0.48, fdr 3e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PINCR]] → it (grade B ⚠); 9 go from it, the strongest it → [[POLH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9037.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.87×** | +9.2 | 3e-17 | 29/40 (A498, LoVo, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.58×** | +6.4 | 4e-08 | 23/40 (C32, NCI-H2347, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.4 | 4e-08 | 18/37 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +6.2 | 8e-08 | 20/38 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.77×** | +5.8 | 6e-07 | 22/40 (SW 900, C32, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +5.8 | 6e-07 | 20/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.57×** | +5.7 | 7e-07 | 17/39 (CFPAC-1, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.73×** | +5.7 | 8e-07 | 20/40 (A498, RKO, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.77×** | +5.7 | 8e-07 | 19/40 (C32, SW 900, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.57×** | +5.6 | 9e-07 | 19/40 (C32, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.73×** | +5.4 | 3e-06 | 22/39 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.64×** | +5.1 | 2e-05 | 19/40 (C32, Hs 766T, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **2.51×** | +5.0 | 2e-05 | 21/41 (LoVo, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.43×** | +4.9 | 3e-05 | 16/40 (C32, CFPAC-1, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +4.9 | 3e-05 | 18/40 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.53×** | +4.8 | 6e-05 | 20/40 (CFPAC-1, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9037.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.323×** | -11.8 | 3e-29 | 34/40 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.505×** | -6.9 | 2e-09 | 23/40 (NCI-H1792, LS 180, …) | rises with dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.348×** | -5.8 | 2e-06 | 21/38 (NCI-H2347, A549, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.358×** | -5.6 | 3e-06 | 23/38 (NCI-H2347, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.371×** | -5.4 | 7e-06 | 22/37 (NCI-H460, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.424×** | -4.7 | 3e-04 | 20/35 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.664×** | -4.3 | 0.001 | 18/40 (NCI-H1792, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.589×** | -4.0 | 0.005 | 10/40 (A498, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **0.715×** | -3.5 | 0.028 | 16/36 (CFPAC-1, NCI-H460, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.561×** | -3.2 | 0.087 | 14/33 (NCI-H2347, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.716×** | -3.1 | 0.087 | 14/39 (SW 900, SHP-77, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.659×** | -3.1 | 0.087 | 13/39 (NCI-H1792, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.662×** | -3.1 | 0.089 | 12/39 (LoVo, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 13.8 | 3 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 5.61× (z +12.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +12.0) | — |
| [[LoVo (line)]] | wt | 14.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 4.89× (z +10.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.127× (z -10.0) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 9.22 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 4.73× (z +8.9) ⚠ cell-cycle shift, explains ~46% of this change | [[Auranofin (drug)]] 5 µM 0.0848× (z -10.1) |
| [[A549 (line)]] | wt | 20.0 | 2 | 0 | [[Amsacrine (drug)]] 5 µM 3.90× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 8.64 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 4.44× (z +10.1) ⚠ cell-cycle shift, explains ~46% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.139× (z -9.5) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 4.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0526× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[HT-29 (line)]] | alt | 9.53 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.133× (z -9.2) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.120× (z -13.1) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 11.0 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 8.15× (z +8.6) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.148× (z -9.0) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDXR]] | +0.73 | +0.62 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[RPS27L]] | +0.72 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[PHLDA3]] | +0.71 | +0.58 / +0.73 | both halves | 8e-06 | **novel candidate** |
| [[ZMAT3]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[PPM1D]] | +0.70 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[RRM2B]] | +0.70 | +0.56 / +0.71 | both halves | 1e-05 | STRING 412 |
| [[ISCU]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[EDA2R]] | +0.68 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[ANKRA2]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[PINCR]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SESN1]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | STRING 470 |
| [[SPATA18]] | +0.61 | +0.48 / +0.62 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHBP1]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[HMBS]] | -0.49 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[SERBP1]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[POLR1E]] | -0.48 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[NAA15]] | -0.47 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[MRPL24]] | -0.47 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[GNPNAT1]] | -0.46 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[UTP14A]] | -0.46 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[TUBA1C]] | -0.45 | -0.47 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PINCR]] | B | PINCR activity raises TP53INP1's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.93× lower at baseline in the lines without PINCR | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[PTCHD4]] | B | PTCHD4 activity raises TP53INP1's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 2.10× lower at baseline in the lines without PTCHD4 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[TOP2A]] | B | TOP2A activity lowers TP53INP1's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens TP53INP1's drug response | lines that do not express PINCR (21) vs lines expressing it (19) | the lines without PINCR respond 0.62× as strongly (z diff +1.18); strongest at Doxorubicin (hydrochloride) 5 µM: 1.16x vs 3.23x (z diff +4.1) | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[MIR34AHG]] | B | MIR34AHG activity raises TP53INP1's level | lines that do not express MIR34AHG (15) vs lines expressing it (35) | 1.44× lower at baseline in the lines without MIR34AHG | 0.071 | ⚠ within organs, on part of the lines; also absent: SPATA18, LINC01876 |
| [[GDF15]] | B | GDF15 activity raises TP53INP1's level | lines that do not express GDF15 (18) vs lines expressing it (32) | 1.36× lower at baseline in the lines without GDF15 | 0.078 | ⚠ within organs, on part of the lines; also absent: PCSK5, ALOX5, LINC03040 |
| [[MDM2]] | C | MDM2's natural level strengthens TP53INP1's drug response | MDM2's natural level across 40 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.50; direction not clear | 0.029 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[GPX1]] | C | GPX1 activity raises TP53INP1's level | lines that do not express GPX1 (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without GPX1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FUCA2; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLH]] | B | TP53INP1 activity raises POLH's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without TP53INP1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[CCNG1]] | B | TP53INP1 activity raises CCNG1's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without TP53INP1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[DDB2]] | B | TP53INP1 activity raises DDB2's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 1.82× lower at baseline in the lines without TP53INP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[SESN1]] | B | TP53INP1 activity raises SESN1's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without TP53INP1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[ZMAT3]] | B | TP53INP1 activity raises ZMAT3's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 2.29× lower at baseline in the lines without TP53INP1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[DCP1B]] | B | TP53INP1 activity raises DCP1B's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without TP53INP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[MIR34AHG]] | B | TP53INP1 activity raises MIR34AHG's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 3.09× lower at baseline in the lines without TP53INP1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[FDXR]] | B | TP53INP1 activity raises FDXR's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 1.88× lower at baseline in the lines without TP53INP1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[ZMAT3]] | B | TP53INP1 activity strengthens ZMAT3's drug response | lines that do not express TP53INP1 (6) vs lines expressing it (38) | the lines without TP53INP1 respond 1.08× as strongly (z diff +0.13); strongest at Idarubicin (hydrochloride) 5 µM: 1.26x vs 2.10x (z diff +4.5) | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.744). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.5, 36.2); signed map (42.1, -24.4). **Vector** length 107, 27.0% of its response variance represented; |z| ≥ 3 in 1,228 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 pathway* (hallmark, mean cos +0.54 to 26); *apoptosis* (hallmark, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.9 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.3 | +9.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.3 | +2.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +4.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.5 | +4.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -11.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.1 | -6.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -5.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -5.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.6 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | tumor protein p53 inducible nuclear protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:94,925,972-94,949,378 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434M1317, FLJ22139, P53DINP1, SIP, TP53INP1A, TP53INP1B, Teap |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 5 pathways, smallest: TP53 Regulates Transcription of Genes Involved in Cytochrome C Release; TP53 Regulates Transcription of Cell Death Genes; Regulation of TP53 Activity through Phosphorylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A56](https://www.uniprot.org/uniprotkb/Q96A56) (Tumor protein p53-inducible nuclear protein 1):

> Antiproliferative and pro-apoptotic protein involved in cell stress response which acts as a dual regulator of transcription and autophagy. Acts as a positive regulator of autophagy. In response to cellular stress or activation of autophagy, relocates to autophagosomes where it interacts with autophagosome-associated proteins GABARAP, GABARAPL1/L2, MAP1LC3A/B/C and regulates autophagy. Acts as an antioxidant and plays a major role in p53/TP53-driven oxidative stress response. Possesses both a …

**Summary**, from NCBI Gene [94241](https://www.ncbi.nlm.nih.gov/gene/94241):

> Predicted to enable antioxidant activity. Involved in autophagic cell death; positive regulation of DNA-templated transcription; and positive regulation of autophagy. Located in autophagosome; cytosol; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18022) · Entrez [94241](https://www.ncbi.nlm.nih.gov/gene/94241) · UniProt [Q96A56](https://www.uniprot.org/uniprotkb/Q96A56) · Ensembl [ENSG00000164938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164938)

## Data

Gene col 9037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9037); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9037]; `tensor/DDL_lfc|DDL_z.npy` [9037]; `embed/gene_vectors.npy` [9037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9037 or target_col == 9037). Every well: [[TP53INP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/TP53INP1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
