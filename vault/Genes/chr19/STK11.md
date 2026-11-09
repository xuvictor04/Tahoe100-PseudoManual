---
symbol: "STK11"
type: "gene"
col: 3961
ensembl_id: "ENSG00000118046"
name: "serine/threonine kinase 11"
location: "19p13.3"
module: 173
arm: "+"
pooled_cpm: 19.48
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/173", "written"]
generated_by: "tahoemap"
---

# STK11

*serine/threonine kinase 11* — 19p13.3

> [!summary] In one line
> STK11 encodes LKB1, the master upstream kinase that activates AMPK and twelve related kinases, and the tumour suppressor whose germline loss causes Peutz-Jeghers syndrome.

## What it is

LKB1 is a serine/threonine kinase that does not work alone: it is an obligate heterotrimer with the pseudokinase STRADα and the scaffold MO25/CAB39, which together activate it and set its localisation. In that form it is largely constitutively active — the always-on upstream element, the regulation sitting in its substrates.

LKB1 phosphorylates the activation-loop threonine of AMPKα, and the equivalent residue in twelve other AMPK-family kinases: the salt-inducible kinases, the MARK/PAR-1 polarity kinases, the BRSKs, the NUAKs and SNRK. The AMPK arm is the best known: as AMP rises relative to ATP, AMPK becomes sensitive to LKB1 phosphorylation, and its activation shuts down anabolic ATP consumption and restrains mTORC1 via TSC2 and raptor. Cells lacking LKB1 fail to activate AMPK under energy stress and lose the associated checkpoint — the core of LKB1's metabolic tumour-suppressor account. The MARK and SIK arms carry polarity and CRTC/HDAC-dependent transcriptional functions.

Germline loss-of-function causes Peutz-Jeghers syndrome: hamartomatous gastrointestinal polyposis, mucocutaneous pigmentation and markedly elevated cancer risk. Somatically it is among the more frequently inactivated genes in lung adenocarcinoma, often co-mutant with KRAS, and in cervical and pancreatic cancers; the STK11/KRAS double-mutant subgroup is immunotherapy-resistant and immune-cold.

## What is uncertain

The attenuation argument is narrower than it appears. The AMPK-to-p53 checkpoint was characterised under energy stress; most compounds here act through DNA damage, replication stress or MDM2 inhibition, and whether LKB1 loss blunts p53's response to those is not established. LKB1 loss plausibly lowers basal and metabolic-stress p53 tone; it has not been shown to damp the responses measured here.

Whether AMPK is the relevant effector for LKB1's tumour suppression is contested: LKB1 has twelve other substrates, in several models the SIK branch accounts for more of the phenotype, and AMPK itself can support or restrain tumour growth by context. "LKB1 loss removes a tumour-suppressive AMPK signal" simplifies an unsettled question. The p53 step is also open: AMPK-dependent p53 serine-15 phosphorylation is reported, but its contribution relative to ATM and ATR at endogenous levels is not well quantified.

One measurement caveat: STK11 transcript level is an unreliable proxy for LKB1 function. Truncating alleles may or may not reduce mRNA through nonsense-mediated decay, and a kinase-impairing missense allele leaves the transcript intact, so an mRNA panel cannot distinguish an LKB1-null line from a functional one.

## References

- Hemminki et al., 1998, Nature — identified a serine/threonine kinase gene defective in Peutz-Jeghers syndrome.
- Jenne et al., 1998, Nature Genetics — independently showed Peutz-Jeghers syndrome is caused by mutations in this novel serine/threonine kinase.
- Lizcano et al., 2004, EMBO Journal — LKB1 is a master kinase activating thirteen AMPK-subfamily kinases, including MARK/PAR-1.
- Shaw et al., 2004, PNAS — LKB1 directly activates AMPK and is required for the apoptotic response to energy stress.
- Jones et al., 2005, Molecular Cell — AMPK activation induces a p53-dependent metabolic checkpoint.
- Skoulidis et al., 2018, Cancer Discovery — STK11/LKB1 loss associates with resistance to PD-1 blockade in KRAS-mutant lung adenocarcinoma.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +17.9, q 0e+00, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.626× (z -9.6, q 3e-19, down in 32 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 0.682× (z -4.1, q 0.006, down in 11 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Resveratrol (drug)]] 0.05 µM in 1 line (SNU-1 0.0683×); [[Belzutifan (drug)]] 5 µM in 1 line (A498 0.124×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (PANC-1 0.474×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SIX5]] (+0.66, fdr 3e-05), [[ERF]] (+0.64, fdr 3e-05), [[GIGYF1]] (+0.63, fdr 3e-05); moves opposite to [[CTNNBL1]] (-0.58, fdr 1e-04), [[IQCB1]] (-0.54, fdr 1e-04), [[ST6GALNAC4]] (-0.53, fdr 1e-04).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MMRN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3961.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +17.9 | 0e+00 | 36/45 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +14.3 | 7e-44 | 32/44 (NCI-H2030, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +10.3 | 1e-22 | 26/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +9.7 | 6e-20 | 25/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +9.0 | 3e-17 | 20/33 (A498, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.33×** | +5.9 | 3e-07 | 21/46 (LS 180, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.32×** | +5.7 | 1e-06 | 18/43 (BT-474, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **1.34×** | +5.2 | 1e-05 | 19/37 (HepG2/C3A, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.29×** | +4.5 | 3e-04 | 8/45 (HOP62, LoVo, …) | inconsistent across doses | position effect removed |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **1.23×** | +4.3 | 8e-04 | 12/45 (MIA PaCa-2, A498, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.23×** | +4.1 | 0.002 | 19/45 (HOP62, SNU-423, …) | top dose only | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.002 | 15/46 (A549, SNU-423, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.22×** | +4.0 | 0.002 | 11/46 (SW480, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.006 | 9/45 (PANC-1, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Fumaric acid (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.006 | 3/45 (PANC-1, CHP-212, …) | inconsistent across doses | position effect removed |
| [[Oxaliplatin (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.006 | 1/44 (PANC-1) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Tolmetin (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.015 | 1/45 (A498) | inconsistent across doses | position effect removed |
| [[crizotinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.051 | 5/46 (NCI-H23, HS-578T, …) | rises with dose |  |
| [[Oxaliplatin (drug)]] 0.05 µM |  | 1.16× | +2.9 | 0.088 | 4/46 (PANC-1, COLO 205, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3961.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Resveratrol (drug)]] 0.05 µM in 1 line (SNU-1 0.0683×); [[Belzutifan (drug)]] 5 µM in 1 line (A498 0.124×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (PANC-1 0.474×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.626×** | -9.6 | 3e-19 | 32/45 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.802×** | -4.4 | 0.003 | 12/45 (LOX-IMVI, NCI-H23, …) | rises with dose | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.843× | -4.3 | 0.003 | 8/46 (HEC-1-A, LOX-IMVI, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.682×** | -4.1 | 0.006 | 11/46 (PANC-1, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.835× | -3.5 | 0.054 | 5/46 (PANC-1, RKO, …) | inconsistent across doses | position effect removed |
| [[Tadalafil (drug)]] 5 µM |  | 0.842× | -3.4 | 0.054 | 9/45 (COLO 205, HS-578T, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.730×** | -3.4 | 0.054 | 8/44 (SW 900, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clonidine (hydrochloride) (drug)]] 5 µM |  | 0.868× | -3.4 | 0.054 | 6/46 (LoVo, LOX-IMVI, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | 0.751× | -3.1 | 0.13 | 4/45 (PANC-1, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | 0.813× | -3.0 | 0.13 | 1/46 (LOX-IMVI) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | 0.755× | -3.0 | 0.13 | 11/42 (A498, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.864× | -3.0 | 0.13 | 7/45 (H4, HEC-1-A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3961. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 14.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +16.5) | — |
| [[NCI-H460 (line)]] | wt | 13.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +13.4) | — |
| [[A-172 (line)]] | wt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +11.5) | — |
| [[A498 (line)]] | wt | 24.7 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.124× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.50× (z +14.1) | — |
| [[HEC-1-A (line)]] | alt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.6) | — |
| [[J82 (line)]] | alt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 21.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.284× (z -8.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[NCI-H1792 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 41.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.474× (z -8.7) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 1 | — | [[Resveratrol (drug)]] 0.05 µM 0.0683× (z -9.6) |
| [[SNU-423 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +16.9) | — |
| [[A-427 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3961), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIX5]] | +0.66 | +0.76 / +0.46 | both halves | 3e-05 |  |
| [[ERF]] | +0.64 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[GIGYF1]] | +0.63 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[GSE1]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[COL11A2]] | +0.61 | +0.65 / +0.46 | both halves | 2e-05 |  |
| [[TRIM8]] | +0.60 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[FBRS]] | +0.59 | +0.56 / +0.37 | both halves | 7e-05 |  |
| [[AKT1S1]] | +0.59 | +0.62 / +0.27 | both halves | 3e-04 | pathway: MTOR signalling; STRING 565 |
| [[MLLT6]] | +0.59 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[RGL2]] | +0.58 | +0.61 / +0.36 | both halves | 1e-04 |  |
| [[ZFTRAF1]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ARHGEF17]] | +0.58 | +0.55 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNBL1]] | -0.58 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[IQCB1]] | -0.54 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[ST6GALNAC4]] | -0.53 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[RNGTT]] | -0.53 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[MKRN2]] | -0.53 | -0.52 / -0.26 | both halves | 3e-04 |  |
| [[CNIH1]] | -0.52 | -0.68 / -0.32 | both halves | 2e-04 |  |
| [[NEIL2]] | -0.51 | -0.51 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[POP1]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[PHB1]] | -0.51 | -0.40 / -0.37 | both halves | 9e-05 |  |
| [[TAF5L]] | -0.50 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[GEMIN5]] | -0.49 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[TMEM161B]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[EDRF1]] | -0.49 | -0.43 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMRN2]] | B | MMRN2 activity raises STK11's level | lines that do not express MMRN2 (11) vs lines expressing it (39) | 1.52× lower at baseline in the lines without MMRN2 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000225751 |
| [[ARHGEF17]] | C | ARHGEF17 activity raises STK11's level | lines that do not express ARHGEF17 (4) vs lines expressing it (46) | 1.98× lower at baseline in the lines without ARHGEF17 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RGS10; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.2, -2.6); signed map (5.0, -6.5). **Vector** length 62.8, 9.84% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +17.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +14.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | +2.7 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.1 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +0.9 | -0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -9.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,177,558-1,228,431 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PJS, LKB1 |
| Gene groups (HGNC) | STK11 family kinases |
| Reactome | 9 pathways, smallest: AMPK inhibits chREBP transcriptional activation activity; FOXO-mediated transcription of cell death genes; Energy dependent regulation of mTOR by LKB1-AMPK |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15831](https://www.uniprot.org/uniprotkb/Q15831) (Serine/threonine-protein kinase STK11):

> Tumor suppressor serine/threonine-protein kinase that controls the activity of AMP-activated protein kinase (AMPK) family members, thereby playing a role in various processes such as cell metabolism, cell polarity, apoptosis and DNA damage response. Acts by phosphorylating the T-loop of AMPK family proteins, thus promoting their activity: phosphorylates PRKAA1, PRKAA2, BRSK1, BRSK2, MARK1, MARK2, MARK3, MARK4, NUAK1, NUAK2, SIK1, SIK2, SIK3 and SNRK but not MELK. Also phosphorylates non-AMPK …

**Summary**, from NCBI Gene [6794](https://www.ncbi.nlm.nih.gov/gene/6794):

> The protein encoded by this gene is a serine/threonine kinase that regulates cell polarity and energy metabolism and functions as a tumor suppressor. Mutations in this gene have been associated with the autosomal dominant Peutz-Jeghers syndrome, as well as with skin, pancreatic, and testicular cancers. [provided by RefSeq, May 2022]

**Accessions** — [HGNC:11389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11389) · Entrez [6794](https://www.ncbi.nlm.nih.gov/gene/6794) · UniProt [Q15831](https://www.uniprot.org/uniprotkb/Q15831) · Ensembl [ENSG00000118046](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118046)

## Data

Gene col 3961: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3961); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3961, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3961]; `tensor/DDL_lfc|DDL_z.npy` [3961]; `embed/gene_vectors.npy` [3961]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3961 or target_col == 3961). Every well: [[STK11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/STK11.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
